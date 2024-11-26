import json
import time
from typing import Optional, Any, TypedDict
from uuid import uuid4

import bcrypt
import jwt
from mongoengine import DoesNotExist

from commons import ApplicationException, RESPONSE_UNAUTHORIZED, \
    RESPONSE_BAD_REQUEST_CODE
from commons.constants import EXP_ATTR, COGNITO_USERNAME, CUSTOM_ROLE_ATTR, \
    CUSTOM_CUSTOMER_ATTR, CUSTOM_LATEST_LOGIN_ATTR, SYSTEM_CUSTOMER
from commons.log_helper import get_logger
from commons.time_helper import utc_iso
from connections.auth_extension.base_auth_client import BaseAuthClient
from models.user import User
from services.ssm_service import SSMService

_LOG = get_logger(__name__)

AUTH_TOKEN_NAME = 'token'
EXPIRATION_IN_MINUTES = 60

USER_NOT_FOUND_MESSAGE = 'No user with username {username} was found'
WRONG_USER_CREDENTIALS_MESSAGE = 'Incorrect username and/or password'
TOKEN_EXPIRED_MESSAGE = 'The incoming token has expired'
UNAUTHORIZED_MESSAGE = 'Unauthorized'


class MongoAndSSMAuthClient(BaseAuthClient):
    class JwtSecret(TypedDict):
        phrase: str

    def __init__(self, ssm_service: SSMService):
        self._ssm = ssm_service

    def _get_jwt_secret(self) -> JwtSecret:
        jwt_secret = self._ssm.get_secret_value(AUTH_TOKEN_NAME)

        if not jwt_secret:
            _LOG.error('Can not find jwt-secret')
            raise ApplicationException(
                code=RESPONSE_UNAUTHORIZED,
                content=WRONG_USER_CREDENTIALS_MESSAGE)
        if isinstance(jwt_secret, dict):
            return jwt_secret
        # isinstance(jwt_secret, str):
        try:
            return json.loads(jwt_secret)
        except json.JSONDecodeError:
            _LOG.error('Invalid jwt-secret format')
            raise ApplicationException(
                code=RESPONSE_UNAUTHORIZED,
                content=WRONG_USER_CREDENTIALS_MESSAGE)

    def decode_token(self, token: str) -> dict:
        jwt_secret = self._get_jwt_secret()
        try:
            return jwt.decode(
                jwt=token,
                key=jwt_secret['phrase'],
                algorithms=['HS256']
            )
        except jwt.exceptions.ExpiredSignatureError:
            raise ApplicationException(
                code=RESPONSE_UNAUTHORIZED,
                content=TOKEN_EXPIRED_MESSAGE,
            )
        except jwt.exceptions.PyJWTError:
            raise ApplicationException(
                code=RESPONSE_UNAUTHORIZED,
                content=UNAUTHORIZED_MESSAGE
            )

    def admin_initiate_auth(self, username: str, password: str) -> dict:
        # todo implement refresh token

        user_item = User.objects.get(user_id=username)
        if not user_item or bcrypt.hashpw(password.encode(),
                                          user_item.password.encode()) != user_item.password.encode():
            _LOG.error(WRONG_USER_CREDENTIALS_MESSAGE)
            raise ApplicationException(
                code=RESPONSE_UNAUTHORIZED,
                content=WRONG_USER_CREDENTIALS_MESSAGE)

        jwt_secret = self._get_jwt_secret()
        self.update_latest_login(username)
        encoded_jwt = jwt.encode(
            payload={
                COGNITO_USERNAME: username,
                CUSTOM_CUSTOMER_ATTR: user_item.customer,
                CUSTOM_ROLE_ATTR: user_item.role,
                CUSTOM_LATEST_LOGIN_ATTR: user_item.latest_login,
                EXP_ATTR: round(time.time()) + EXPIRATION_IN_MINUTES * 60
            },
            key=jwt_secret['phrase'],
            algorithm='HS256'
        )
        return {
            'AuthenticationResult': {
                'IdToken': encoded_jwt, 'RefreshToken': []
            }
        }

    @staticmethod
    def _set_password(user: User, password: str):
        user.password = bcrypt.hashpw(password.encode(),
                                      bcrypt.gensalt()).decode()

    def admin_delete_user(self, username: str):
        User(hash_key=username).delete()

    def respond_to_auth_challenge(self, challenge_name: str):
        pass

    def sign_up(self, username, password, customer, role, tenants=None):
        user = User()
        user.user_id = username
        self._set_password(user, password)
        user.customer = customer
        user.role = role
        user.sub = str(uuid4())
        User.save(user)

    @staticmethod
    def _get_user(username: str) -> Optional[User]:
        try:
            return User.objects.get(user_id=username)
        except DoesNotExist:
            return

    def _get_user_attr(self, username: str, attr: str) -> Any:
        return getattr(self._get_user(username), attr, None)

    def is_user_exists(self, username: str) -> bool:
        return bool(self._get_user(username))

    def get_user_id(self, username: str):
        return self._get_user_attr(username, 'sub')

    def list_users(self, attributes_to_get=None):
        try:
            users = list(User.objects.all())
        except:
            return
        return [user.get_dto() for user in users]

    def get_user_role(self, username: str):
        return self._get_user_attr(username, 'role')

    def get_user_customer(self, username: str):
        return self._get_user_attr(username, 'customer')

    def get_user_latest_login(self, username: str):
        return self._get_user_attr(username, 'latest_login')

    def update_role(self, username: str, role: str):
        user = self._get_user(username)
        if not user:
            _LOG.warning(USER_NOT_FOUND_MESSAGE.format(username=username))
            return
        user.role = role
        user.save()

    def update_customer(self, username: str, customer: str):
        user = self._get_user(username)
        if not user:
            _LOG.warning(USER_NOT_FOUND_MESSAGE.format(username=username))
            return
        user.customer = customer
        user.save()

    def update_latest_login(self, username: str):
        user = self._get_user(username)
        if not user:
            _LOG.warning(USER_NOT_FOUND_MESSAGE.format(username=username))
            return
        user.latest_login = utc_iso()
        user.save()

    def delete_role(self, username: str):
        user = self._get_user(username)
        if not user:
            _LOG.warning(USER_NOT_FOUND_MESSAGE.format(username=username))
            return
        user.role = None
        user.save()

    def delete_customer(self, username: str):
        user = self._get_user(username)
        if not user:
            _LOG.warning(USER_NOT_FOUND_MESSAGE.format(username=username))
            return
        user.customer = None
        user.save()

    def set_password(self, username: str, password: str,
                     permanent: bool = True):
        user = User.objects.get(user_id=username)
        self._set_password(user, password)
        user.save()

    def is_system_user_exists(self) -> bool:
        """Checks whether user with customer=SYSTEM_CUSTOMER already exists"""
        scan_results = list(User.objects(User.customer == SYSTEM_CUSTOMER))
        if not scan_results:
            return False
        number_of_system_users = len(scan_results)
        if number_of_system_users == 0:
            return False
        elif number_of_system_users == 1:
            return True
        elif number_of_system_users > 1:
            raise AssertionError("Only one SYSTEM user must be!")

    def get_system_user(self):
        users = User.objects(User.customer == SYSTEM_CUSTOMER)
        try:
            return next(users).user_id
        except StopIteration:
            _LOG.info("No SYSTEM user was found")
            return None

    def get_user(self, username):
        user = self._get_user(username)
        if not user:
            _LOG.error(f'No user with username {username} was found')
            raise ApplicationException(
                code=RESPONSE_BAD_REQUEST_CODE,
                content=f'No user with username {username} was found')
        return user.get_dto()

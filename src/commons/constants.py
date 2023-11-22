USER_ID_ATTR = 'user_id'
NAME_ATTR = 'name'
SETTING_IAM_PERMISSIONS = 'IAM_PERMISSIONS'
SETTING_LAST_SHAPE_UPDATE = 'LAST_SHAPE_UPDATE'
SETTING_AWS_INSTANCES_DATA = 'AWS_INSTANCES_DATA'
SETTING_AWS_INSTANCE_PRICES = 'AWS_INSTANCE_PRICES'
SETTING_MAESTRO_APPLICATION_ID = 'APPLICATION_ID'
EXPAND_ATTR = 'expand'

GET_METHOD = 'GET'
POST_METHOD = 'POST'
PATCH_METHOD = 'PATCH'
DELETE_METHOD = 'DELETE'

ID_ATTR = 'id'
USERNAME_ATTR = 'username'
PASSWORD_ATTR = 'password'
ID_TOKEN_ATTR = 'id_token'
REFRESH_TOKEN_ATTR = 'refresh_token'
ROLE_ATTR = 'role'

ALGORITHM_ATTR = 'algorithm'
EXPIRATION_ATTR = 'expiration'
PERMISSIONS_ATTR = 'permissions'
PERMISSIONS_ADMIN_ATTR = 'permissions_admin'
PERMISSIONS_TO_ATTACH = 'permissions_to_attach'
PERMISSIONS_TO_DETACH = 'permissions_to_detach'
POLICIES_TO_ATTACH = 'policies_to_attach'
POLICIES_TO_DETACH = 'policies_to_detach'
POLICIES_ATTR = 'policies'
RESOURCE_ATTR = 'resource'
CUSTOMER_ATTR = 'customer'
CUSTOMERS_ATTR = 'customers'
REGION_ATTR = 'region'
CLOUD_ATTR = 'cloud'
CLOUDS_ATTR = 'clouds'
DETAILED_ATTR = 'detailed'
OS_ATTR = 'os'
DESCRIPTION_ATTR = 'description'
CONNECTION_ATTR = 'connection'
HOST_ATTR = 'host'
PORT_ATTR = 'port'
PROTOCOL_ATTR = 'protocol'
ATTACHMENT_MODEL_ATTR = 'attachment_model'

SERVICE_ATTR = 'service'
TYPE_ATTR = 'type'
TYPES_ATTR = 'types'
ACCESS_ATTR = 'access'

BUCKET_NAME_ATTR = 'bucket_name'
PREFIX_ATTR = 'prefix'

DATA_SOURCE_ATTR = 'data_source'
STORAGE_ATTR = 'storage'
MODEL_ATTR = 'model'
SCHEDULE_ATTR = 'schedule'
ANALYSIS_SPECS_ATTR = 'analysis_specs'
JOB_DEFINITION_ATTR = 'job_definition'
PARAM_NATIVE_JOB_ID = 'jobId'
TENANT_ATTR = 'tenant'
TENANTS_ATTR = 'tenants'
SCAN_TIMESTAMP_ATTR = 'scan_timestamp'
SCAN_FROM_DATE_ATTR = 'scan_from_date'
SCAN_TO_DATE_ATTR = 'scan_to_date'
INSTANCE_ID_ATTR = 'instance_id'
SCAN_CLOUDS_ATTR = 'scan_clouds'
APPLICATION_ID_ATTR = 'application_id'
MAESTRO_RIGHTSIZER_APPLICATION_TYPE = 'RIGHTSIZER'
INPUT_STORAGE_ATTR = 'input_storage'
OUTPUT_STORAGE_ATTR = 'output_storage'
ADDED_AT_ATTR = 'added_at'
RECOMMENDATION_TYPE_ATTR = 'recommendation_type'
JOB_ID_ATTR = 'job_id'
LIMIT_ATTR = 'limit'

RULE_ACTION_ATTR = 'rule_action'
CONDITION_ATTR = 'condition'
FIELD_ATTR = 'field'
VALUE_ATTR = 'value'

REQUIRED_DATA_ATTRS_ATTR = 'required_data_attributes'
METRIC_ATTRS_ATTR = 'metric_attributes'
TIMESTAMP_ATTR = 'timestamp_attribute'
ACTION_ATTR = 'action'
REPORT_TYPE_ATTR = 'report_type'
REPORT_TYPE_INSTANCE_SHAPE = 'instance_shape'
LICENSED_ATTR = 'licensed'

MONGODB_CONNECTION_URI_PARAMETER = 'r8s_mongodb_connection_uri'
JSON_EXTENSION = '.json'
JSON_LINES_EXTENSION = '.jsonl'

CLOUD_AWS = 'AWS'
CLOUD_AZURE = 'AZURE'
CLOUD_GOOGLE = 'GOOGLE'

CLOUDS = [CLOUD_AWS, CLOUD_AZURE, CLOUD_GOOGLE]

DEFAULT_DATA_ATTRIBUTES = [
    "instance_id",
    "instance_type",
    "timestamp",
    "cpu_load",
    "memory_load",
    "net_output_load",
    "avg_disk_iops",
    "max_disk_iops"
]
DEFAULT_METRIC_ATTRIBUTES = [
    "cpu_load",
    "memory_load",
    "net_output_load",
    "avg_disk_iops"
]

METRIC_FORMAT_ATTR = 'metric_format'
DELIMITER_ATTR = 'delimiter'
SKIP_INITIAL_SPACE_ATTR = 'skipinitialspace'
LINE_TERMINATOR_ATTR = 'lineterminator'
QUOTE_CHAR_ATTR = 'quotechar'
QUOTING_ATTR = 'quoting'
ESCAPE_CHAR_ATTR = 'escapechar'
DOUBLE_QUOTE_ATTR = 'doublequote'

METRIC_FORMAT_ATTRS = [DELIMITER_ATTR, SKIP_INITIAL_SPACE_ATTR,
                       LINE_TERMINATOR_ATTR, QUOTE_CHAR_ATTR, QUOTING_ATTR,
                       ESCAPE_CHAR_ATTR, DOUBLE_QUOTE_ATTR]

CLUSTERING_SETTINGS_ATTR = 'clustering_settings'
MAX_CLUSTERS_ATTR = 'max_clusters'
WCSS_KMEANS_INIT_ATTR = 'wcss_kmeans_init'
WCSS_KMEANS_MAX_ITER_ATTR = 'wcss_kmeans_max_iter'
WCSS_KMEANS_N_INIT_ATTR = 'wcss_kmeans_n_init'
KNEE_INTERP_METHOD_ATTR = 'knee_interp_method'
KNEE_POLYMONIAL_DEGREE_ATTR = 'knee_polynomial_degree'

CLUSTERING_SETTINGS_ATTRS = [
    MAX_CLUSTERS_ATTR, WCSS_KMEANS_INIT_ATTR, WCSS_KMEANS_N_INIT_ATTR,
    WCSS_KMEANS_MAX_ITER_ATTR, KNEE_INTERP_METHOD_ATTR,
    KNEE_POLYMONIAL_DEGREE_ATTR]

RECOMMENDATION_SETTINGS_ATTR = 'recommendation_settings'
RECORD_STEP_MINUTES_ATTR = 'record_step_minutes'
THRESHOLDS_ATTR = 'thresholds'
MIN_ALLOWED_DAYS_ATTR = 'min_allowed_days'
MAX_DAYS_ATTR = 'max_days'
MIN_ALLOWED_DAYS_SCHEDULE_ATTR = 'min_allowed_days_schedule'
IGNORE_SAVINGS_ATTR = 'ignore_savings'
MAX_RECOMMENDED_SHAPES_ATTR = 'max_recommended_shapes'
SHAPE_COMPATIBILITY_RULE_ATTR = 'shape_compatibility_rule'
SHAPE_SORTING_ATTR = 'shape_sorting'
USE_PAST_RECOMMENDATIONS_ATTR = 'use_past_recommendations'
USE_INSTANCE_TAGS_ATTR = 'use_instance_tags'
ANALYSIS_PRICE_ATTR = 'analysis_price'
IGNORE_ACTIONS_ATTR = 'ignore_actions'
TARGET_TIMEZONE_NAME_ATTR = 'target_timezone_name'
DISCARD_INITIAL_ZEROS_ATTR = 'discard_initial_zeros'
FORBID_CHANGE_SERIES_ATTR = 'forbid_change_series'
FORBID_CHANGE_FAMILY_ATTR = 'forbid_change_family'

RECOMMENDATION_SETTINGS_ATTRS = [
    RECORD_STEP_MINUTES_ATTR, THRESHOLDS_ATTR, MIN_ALLOWED_DAYS_ATTR,
    MAX_DAYS_ATTR, MIN_ALLOWED_DAYS_SCHEDULE_ATTR, IGNORE_SAVINGS_ATTR,
    MAX_RECOMMENDED_SHAPES_ATTR, SHAPE_COMPATIBILITY_RULE_ATTR,
    SHAPE_SORTING_ATTR, USE_PAST_RECOMMENDATIONS_ATTR,
    USE_INSTANCE_TAGS_ATTR, ANALYSIS_PRICE_ATTR, TARGET_TIMEZONE_NAME_ATTR,
    IGNORE_ACTIONS_ATTR, DISCARD_INITIAL_ZEROS_ATTR,
    FORBID_CHANGE_FAMILY_ATTR, FORBID_CHANGE_SERIES_ATTR
]

RULE_ACTION_ALLOW = 'allow'
RULE_ACTION_DENY = 'deny'
RULE_ACTION_PRIORITIZE = 'prioritize'

ALLOWED_RULE_ACTIONS = (RULE_ACTION_ALLOW, RULE_ACTION_DENY,
                        RULE_ACTION_PRIORITIZE)

RULE_CONDITION_CONTAINS = 'contains'
RULE_CONDITION_NOT_CONTAINS = 'not_contains'
RULE_CONDITION_EQUALS = 'equals'
RULE_CONDITION_MATCHES = 'matches'
RULE_CONDITION_NOT_MATCHES = 'not_matches'

ALLOWED_RULE_CONDITIONS = (
    RULE_CONDITION_CONTAINS, RULE_CONDITION_NOT_CONTAINS,
    RULE_CONDITION_EQUALS, RULE_CONDITION_MATCHES, RULE_CONDITION_NOT_MATCHES)

ALLOWED_SHAPE_FIELDS = ('name', 'family_type', 'physical_processor',
                        'architecture')
SCOPE_ATTR = 'scope'
PARENT_ID_ATTR = 'parent_id'
PARENT_SCOPE_ALL = 'ALL_TENANTS'
PARENT_SCOPE_SPECIFIC_TENANT = 'SPECIFIC_TENANT'
ALLOWED_PARENT_SCOPES = (PARENT_SCOPE_ALL, PARENT_SCOPE_SPECIFIC_TENANT)
CLOUD_ALL = 'ALL'

CPU_ATTR = 'cpu'
MEMORY_ATTR = 'memory'
NETWORK_THROUGHPUT_ATTR = 'network_throughput'
IOPS_ATTR = 'iops'
FAMILY_TYPE_ATTR = 'family_type'
PHYSICAL_PROCESSOR_ATTR = 'physical_processor'
ARCHITECTURE_ATTR = 'architecture'

SHAPE_ATTRIBUTES = (NAME_ATTR, CPU_ATTR, MEMORY_ATTR, NETWORK_THROUGHPUT_ATTR,
                    IOPS_ATTR, FAMILY_TYPE_ATTR,
                    PHYSICAL_PROCESSOR_ATTR, ARCHITECTURE_ATTR)
ON_DEMAND_ATTR = 'on_demand'

SHAPE_PRICE_ATTRIBUTES = (CUSTOMER_ATTR, NAME_ATTR, CLOUD_ATTR, REGION_ATTR,
                          OS_ATTR, ON_DEMAND_ATTR)

SUSPICIOUS_PRICE_PER_CPU_THRESHOLD = 0.75
CHECK_TYPE_APPLICATION = 'APPLICATION'
CHECK_TYPE_PARENT = 'PARENT'
CHECK_TYPE_STORAGE = 'STORAGE'
CHECK_TYPE_SHAPE = 'SHAPE'
CHECK_TYPE_SHAPE_UPDATE_DATE = 'SHAPE_UPDATE_DATE'
CHECK_TYPE_OPERATION_MODE = 'OPERATION_MODE'

CHECK_TYPES = (CHECK_TYPE_APPLICATION, CHECK_TYPE_PARENT, CHECK_TYPE_STORAGE,
               CHECK_TYPE_SHAPE, CHECK_TYPE_OPERATION_MODE,
               CHECK_TYPE_SHAPE_UPDATE_DATE)

ACTION_SCHEDULE = 'SCHEDULE'
ACTION_SHUTDOWN = 'SHUTDOWN'
ACTION_SCALE_UP = 'SCALE_UP'
ACTION_SCALE_DOWN = 'SCALE_DOWN'
ACTION_CHANGE_SHAPE = 'CHANGE_SHAPE'
ACTION_SPLIT = 'SPLIT'
ACTION_EMPTY = 'NO_ACTION'
ACTION_ERROR = 'ERROR'

ALLOWED_ACTIONS = [ACTION_SCHEDULE, ACTION_SHUTDOWN, ACTION_SCALE_UP,
                   ACTION_SCALE_DOWN, ACTION_CHANGE_SHAPE, ACTION_SPLIT,
                   ACTION_EMPTY, ACTION_ERROR]

FEEDBACK_STATUS_ATTR = 'feedback_status'

MAIL_REPORT_DEFAULT_PROCESSING_DAYS = 7
MAIL_REPORT_DEFAULT_HIGH_PRIORITY_THRESHOLD = 10
RULE_ID_ATTR = 'rule_id'
INSTANCE_TYPE_ATTR = 'instance_type'

ENV_SERVICE_MODE = 'SERVICE_MODE'
DOCKER_SERVICE_MODE, SAAS_SERVICE_MODE = 'docker', 'saas'

ENV_MONGODB_USER = 'MONGO_USER'
ENV_MONGODB_PASSWORD = 'MONGO_PASSWORD'
ENV_MONGODB_URL = 'MONGO_URL'  # host:port
ENV_MONGODB_DATABASE = 'MONGO_DATABASE'

ENV_MINIO_HOST = 'MINIO_HOST'
ENV_MINIO_PORT = 'MINIO_PORT'
ENV_MINIO_ACCESS_KEY = 'MINIO_ACCESS_KEY'
ENV_MINIO_SECRET_ACCESS_KEY = 'MINIO_SECRET_ACCESS_KEY'

ENV_VAULT_TOKEN = 'VAULT_TOKEN'
ENV_VAULT_HOST = 'VAULT_URL'
ENV_VAULT_PORT = 'VAULT_SERVICE_SERVICE_PORT'

ENV_TENANT_CUSTOMER_INDEX = 'tenants_customer_name_index_rcu'
ENV_LM_TOKEN_LIFETIME_MINUTES = 'lm_token_lifetime_minutes'
EXP_ATTR = 'exp'

# cognito
COGNITO_USERNAME = 'cognito:username'
CUSTOM_ROLE_ATTR = 'custom:role'
CUSTOM_CUSTOMER_ATTR = 'custom:customer'
CUSTOM_LATEST_LOGIN_ATTR = 'custom:latest_login'

SYSTEM_CUSTOMER = 'SYSTEM'

ENV_MAX_NUMBER_OF_JOBS_ON_PREM = 'MAX_NUMBER_OF_JOBS'
BATCH_ENV_SUBMITTED_AT = 'SUBMITTED_AT'
BATCH_ENV_JOB_ID = 'AWS_BATCH_JOB_ID'

REPORT_RESOURCE_ID_ATTR = 'resource_id'
REPORT_RESOURCE_TYPE_ATTR = 'resource_type'
REPORT_RESOURCE_TYPE_INSTANCE = 'INSTANCE'
REPORT_SOURCE_ATTR = 'source'
REPORT_SOURCE_RIGHTSIZER = 'RIGHTSIZER'
REPORT_SEVERITY_ATTR = 'severity'
REPORT_SEVERITY = 'MEDIUM'
REPORT_RECOMMENDATION_ATTR = 'recommendation'

# License Manager
LICENSE_KEY_ATTR = 'license_key'
LICENSE_KEYS_ATTR = 'license_keys'
TENANT_LICENSE_KEY_ATTR = 'tenant_license_key'
TENANT_LICENSE_KEYS_ATTR = 'tenant_license_keys'
AUTHORIZATION_PARAM = 'authorization'
STATUS_ATTR = 'status'
ALGORITHM_ID_ATTR = 'algorithm_id'

KID_ATTR = 'kid'
ALG_ATTR = 'alg'
TYP_ATTR = 'typ'

TOKEN_DATE_ATTR = 'token_date'
CLIENT_TOKEN_ATTR = 'client-token'
STAGE_ATTR = 'stage'
KEY_ID_ATTR = 'key_id'
B64ENCODED_ATTR = 'b64_encoded'

ALLOWED_ATTR = 'allowed'
FORBIDDEN_ATTR = 'forbidden'
REMAINING_BALANCE_ATTR = 'remaining_balance'
TOKEN_ATTR = 'token'

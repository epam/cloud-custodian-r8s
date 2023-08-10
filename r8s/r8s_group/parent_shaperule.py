import click

from r8s_group import cli_response, ViewCommand
from r8s_service.constants import ALLOWED_RULE_ACTIONS, \
    ALLOWED_SHAPE_FIELDS, ALLOWED_RULE_CONDITIONS, AVAILABLE_CLOUDS


@click.group(name='shape_rule')
def shape_rule():
    """Manages RIGHTSIZER Parent Shape rule Entity"""


@shape_rule.command(cls=ViewCommand, name='describe')
@click.option('--parent_id', '-pid', type=str,
              help='Parent id to describe shape rules.')
@click.option('--rule_id', '-rid', type=str,
              help='Rule id to describe.')
@cli_response()
def describe(parent_id=None, rule_id=None):
    """
    Describes a R8s parent shape rules.
    """
    from r8s_service.initializer import init_configuration
    return init_configuration().shape_rule_get(
        parent_id=parent_id, rule_id=rule_id)


@shape_rule.command(cls=ViewCommand, name='add')
@click.option('--parent_id', '-pid', type=str,
              help='Parent id to create shape rule in.')
@click.option('--cloud', '-c', type=click.Choice(AVAILABLE_CLOUDS),
              required=True, help='Shape rule cloud')
@click.option('--action', '-a', required=True,
              type=click.Choice(ALLOWED_RULE_ACTIONS),
              help="Shape rule action.")
@click.option('--condition', '-cd', required=True,
              type=click.Choice(ALLOWED_RULE_CONDITIONS),
              help="Shape rule condition.")
@click.option('--field', '-f', required=True,
              type=click.Choice(ALLOWED_SHAPE_FIELDS),
              help="Shape rule field.")
@click.option('--value', '-v', required=True,
              type=str,
              help="Shape rule filter value.")
@cli_response()
def add(parent_id, cloud, action, condition, field, value):
    """
    Creates a R8s Shape rule.
    """
    from r8s_service.initializer import init_configuration

    return init_configuration().shape_rule_post(
        parent_id=parent_id,
        cloud=cloud,
        action=action,
        condition=condition,
        field=field,
        value=value
    )


@shape_rule.command(cls=ViewCommand, name='update')
@click.option('--rule_id', '-rid', type=str, required=True,
              help='Shape rule id to update.')
@click.option('--parent_id', '-pid', type=str,
              help='Parent id to update shape rule in.')
@click.option('--action', '-a', required=False,
              type=click.Choice(ALLOWED_RULE_ACTIONS),
              help="Shape rule action.")
@click.option('--condition', '-cd', required=False,
              type=click.Choice(ALLOWED_RULE_CONDITIONS),
              help="Shape rule condition.")
@click.option('--field', '-f', required=False,
              type=click.Choice(ALLOWED_SHAPE_FIELDS),
              help="Shape rule field.")
@click.option('--value', '-v', required=False,
              type=str,
              help="Shape rule filter value.")
@cli_response()
def update(rule_id, parent_id, action, condition, field, value):
    """
    Updates a R8s Shape rule.
    """
    from r8s_service.initializer import init_configuration

    return init_configuration().shape_rule_patch(
        parent_id=parent_id,
        rule_id=rule_id,
        action=action,
        condition=condition,
        field=field,
        value=value
    )


@shape_rule.command(cls=ViewCommand, name='delete')
@click.option('--rule_id', '-rid', type=str, required=True,
              help='Shape rule id to delete')
@click.option('--parent_id', '-pid', type=str,
              help='Parent id to delete shape rule from.')
@cli_response()
def delete(rule_id, parent_id):
    """
    Deletes r8s shape rule.
    """
    from r8s_service.initializer import init_configuration
    return init_configuration().shape_rule_delete(rule_id=rule_id,
                                                  parent_id=parent_id)


@shape_rule.command(cls=ViewCommand, name='dry_run')
@click.option('--parent_id', '-pid', type=str, required=True,
              help='Parent id to perform dry run on shape rules')
@click.option('--cloud', '-c', type=click.Choice(AVAILABLE_CLOUDS),
              required=True, help='Cloud to perform dry run.')
@cli_response()
def dry_run(parent_id, cloud):
    """
    Describes shapes that satisfy all of the specified Parent rules for cloud.
    """
    from r8s_service.initializer import init_configuration
    return init_configuration().shape_rule_dry_run_get(
        parent_id=parent_id, cloud=cloud)

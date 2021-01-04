import click 
import pdb

from users.services import UserService
from users.models import User

@click.group()
def users():
    """manages the users life cycle."""
    pass

@users.command()
@click.option('-n', '--name',
            type = str,
            prompt= True,
            help = 'The client name'
            )
@click.option('-ls', '--last_name',
            type = str,
            prompt= True,
            help = 'The client last name'
            )
@click.option('-i', '--identification',
            type = str,
            prompt= True,
            help = 'The client identification'
            )
@click.option('-pn', '--phone_number',
            type = str,
            prompt= True,
            help = 'The client phone number'
            )
@click.option('-w', '--wight',
            type = str,
            prompt= True,
            help = 'The client wight'
            )
@click.option('-h', '--height',
            type = str,
            prompt= True,
            help = 'The client height'
            )
@click.option('-a', '--age',
            type = str,
            prompt= True,
            help = 'The client age'
            )
@click.pass_context
def create(ctx, name , last_name, identification, phone_number, wight, height, age):
    """creates a new client."""
    user = User(name, last_name, identification, phone_number, wight, height, age)
    user_service = UserService(ctx.obj['table_name'])

    user_service.create_user(user)

@users.command()
@click.pass_context
def list(ctx):
    user_service = UserService(ctx.obj['table_name'])
    list_users = user_service.list_user()

    click.echo('       UID        |     NAME     |    lAST NAME    |     IDENTIFICATION     ')
    click.echo('*'* 80)

    for user in list_users:
        click.echo('{uid} | {name} | {last_name} | {identification} '.format(
            uid = user['uid'],
            name = user['name'],
            last_name = user['last_name'],
            identification = user['identification']
        ))

@users.command()
@click.argument('user_uid',
                type= str)
@click.pass_context
def update(ctx, user_uid):
    """updates a client."""
    user_service = UserService(ctx.obj['table_name'])

    users_list = user_service.list_user()

    user = [user for user in users_list if user['uid'] == user_uid]
    #pdb.set_trace()
    if user:
        del user[0]['uid']
        user_updated = _update_user_flow(User(**user[0]))
        user_service.update_user(user_updated)

        click.echo('user update succesfully')     
    else:
        click.echo('user not found.')

def _update_user_flow(user):
    click.echo('Just modify the field that you want to change, leave empty the field if you dont want to change it')

    user.name = click.prompt('wight', type=str, default=user.name)
    user.height = click.prompt('height', type=str, default= user.height)
    user.age = click.prompt('age', type=str, default= user.age)

    return user


@users.command()
@click.argument(
    'user_ident',
    type=str
)
@click.pass_context
def delete(ctx, user_ident):
    """deletes a client."""
    user_service = UserService(ctx.obj['table_name'])
    users_list = user_service.list_user()

    user = [user for user in users_list if user_ident == user['identification']]

    if user:
        del user[0]['uid']
        
        user_service.delete_user(user_ident)

        click.echo('user has been deleted')     
    else:
        click.echo('user not found.')

all = users
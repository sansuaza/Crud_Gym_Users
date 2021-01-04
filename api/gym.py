import click

#commands
from users import commands as users_commands
TABLE_NAME= ".clients.csv"

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['table_name'] = TABLE_NAME

cli.add_command(users_commands.all)
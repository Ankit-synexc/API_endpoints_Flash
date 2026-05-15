from models.echo_schema import Echo
from services import echo_services

def echo(body: Echo):
    return echo_services.process_echo(body.message , body.data)


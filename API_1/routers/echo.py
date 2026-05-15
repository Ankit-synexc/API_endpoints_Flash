from fastapi import APIRouter
from models.echo_schema import EchoResponse,Echo
from controllers import echo_controller

router = APIRouter()

@router.post('/echo' , response_model=EchoResponse)
def echo(body: Echo):
    return echo_controller.echo(body)
from utils.helpers import utc_now

def process_echo(message: str , data : dict) -> dict:
    return {
        "echo_message" : message,
        "echo_data" : data,
        "timestamp" : utc_now()
    }
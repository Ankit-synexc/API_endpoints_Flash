from utils.helpers import utc_now , uptime

def fetch_health() -> dict:
    return{
        "status": "ok",
        "uptime_seconds" : uptime(),
        "timestamp" : utc_now(),
    }

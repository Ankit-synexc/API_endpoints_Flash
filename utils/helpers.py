from datetime import datetime , timezone
import time
import uuid

SERVER_START = time.time()

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def uptime() -> float:
    return round(time.time() - SERVER_START , 2 )

def generate_id() -> str:
    return str(uuid.uuid4())[:8]
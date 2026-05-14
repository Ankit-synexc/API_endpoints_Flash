from services import health_services

def get_health():
    return health_services.fetch_health()
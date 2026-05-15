from services.iris_services import perform_prediction

async def get_prediction(payload):
    return await perform_prediction(payload)
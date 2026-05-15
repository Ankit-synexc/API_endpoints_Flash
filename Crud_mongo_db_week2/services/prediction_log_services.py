from models.Prediction_log_schema import PredictionLog

async def predict_iris(features):
    log_entry = PredictionLog(
        sepal_length=features.sepal_length,
        sepal_width=features.sepal_width,
        petal_length=features.petal_length,
        petal_width=features.petal_width,

    )
    await log_entry.insert()
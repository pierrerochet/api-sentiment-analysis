from datetime import datetime

from fastapi import APIRouter, Request

from api.logger import logger
from api.models import TextIn, TextOut

sentiment = APIRouter()


def predict(input_text, model):
    logger.info("\tModel prediction ...")
    start_time = datetime.now()
    label = int(model.predict([input_text])[0])
    end_time = datetime.now()
    inference_time = end_time - start_time
    logger.info(f"\tModel predicted with inference: {inference_time}")
    return label, inference_time


@sentiment.post("/predict", response_model=TextOut)
async def predict_text(input_text: TextIn, request: Request):
    text = input_text.text
    model = request.app.state.model
    label, inference_time = predict(text, model)

    return {
        "text": text,
        "ml_tags": {
            "sentiment": {
                "label": label,
                "inference_time": inference_time,
            }
        },
        "time": datetime.now(),
    }

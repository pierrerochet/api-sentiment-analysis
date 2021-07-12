import datetime
from typing import Dict

from pydantic import BaseModel
from api import __version__, __name__


class Root(BaseModel):
    message = f"Welcome to the {__name__} !"
    version = __version__


class TextIn(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {"text": "C'est un très bon produit, je recommande !"}
        }


class TextOut(BaseModel):
    text: str
    ml_tags: Dict[str, dict]
    time: datetime.datetime

    class Config:
        schema_extra = {
            "example": {
                "text": "C'est un très bon produit, je recommande !",
                "ml_tags": {
                    "sentiment": {
                        "label": 5,
                        "inference_time": "0.007003",
                    }
                },
                "time": "2021-02-10T10:51:04.318614",
            }
        }

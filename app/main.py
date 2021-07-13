from fastapi import FastAPI
import dill as pickle
from api.models import Root
from api.routes import sentiment
from api.logger import logger
from fastapi.middleware.cors import CORSMiddleware


TAGS_METADATA = [
    {
        "name": "Predict Sentiment",
        "description": "Get the sentiment from a message",
    }
]

app = FastAPI(
    title="API sentiment comment",
    description="Get the sentiment from a comment",
    openapi_tags=TAGS_METADATA,
    version="0.1.0",
    openapi_url="/api/v1/sentiment/openapi.json",
    docs_url="/api/v1/sentiment/docs",
)

origins = [
    "http://localhost:8880",
    "http://172.22.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def load_model():
    logger.info("\tStart loading model ...")
    model_path = "./ml_models/one-vs-rest-20210710-013647/model.pkl"
    with open(model_path, "rb") as model_file:
        app.state.model = pickle.load(model_file)
    logger.info("\tModel loaded successfully")


@app.get("/api/v1/sentiment", response_model=Root)
async def root():
    return {}


app.include_router(
    sentiment, prefix="/api/v1/sentiment", tags=["Predict Sentiment"]
)
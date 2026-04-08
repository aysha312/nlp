from fastapi import FastAPI
from routes.routes import (
    sentiment_router,
    ner_router,
    classification_router,
    combined_router
)

app = FastAPI()

app.include_router(sentiment_router)
app.include_router(ner_router)
app.include_router(classification_router)
app.include_router(combined_router)
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from services.nlp_services import analyze_sentiment, recognize_entities, classify_text
from models.models import TextInput, ClassificationInput
from core.token import auth_scheme, API_TOKEN

sentiment_router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

@sentiment_router.post("/")
def sentiment_analysis(payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"result": analyze_sentiment(payload.text)}


ner_router = APIRouter(prefix="/ner", tags=["NER"])

@ner_router.post("/")
def entity_recognition(payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"entities": recognize_entities(payload.text)}


classification_router = APIRouter(prefix="/classification", tags=["Classification"])

@classification_router.post("/")
def classification(payload: ClassificationInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"label": classify_text(payload.text)}


combined_router = APIRouter(prefix="/combined", tags=["Combined"])

@combined_router.post("/")
def combined_analysis(payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    return {
        "sentiment": analyze_sentiment(payload.text),
        "entities": recognize_entities(payload.text),
        "classification": classify_text(payload.text)
    }
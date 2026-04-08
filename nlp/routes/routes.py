from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials
from services.nlp_services import analyze_sentiment, recognize_entities, classify_text
from models.models import TextInput, ClassificationInput
from core.token import auth_scheme, API_TOKEN
from limiter.limiter import limiter
from slowapi.errors import RateLimitExceeded

sentiment_router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

@sentiment_router.post("/")
@limiter.limit("5/minute")
def sentiment_analysis(request: Request, payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"result": analyze_sentiment(payload.text)}


ner_router = APIRouter(prefix="/ner", tags=["NER"])

@ner_router.post("/")
@limiter.limit("5/minute")
def entity_recognition(request: Request, payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"entities": recognize_entities(payload.text)}


classification_router = APIRouter(prefix="/classification", tags=["Classification"])

@classification_router.post("/")
@limiter.limit("5/minute")
def classification(request: Request, payload: ClassificationInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"label": classify_text(payload.text)}


combined_router = APIRouter(prefix="/combined", tags=["Combined"])

@combined_router.post("/")
@limiter.limit("5/minute")
def combined_analysis(request: Request, payload: TextInput, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if token.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    return {
        "sentiment": analyze_sentiment(payload.text),
        "entities": recognize_entities(payload.text),
        "classification": classify_text(payload.text)
    }

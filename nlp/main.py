from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from limiter.limiter import limiter
from routes.routes import (
    sentiment_router,
    ner_router,
    classification_router,
    combined_router
)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.include_router(sentiment_router)
app.include_router(ner_router)
app.include_router(classification_router)
app.include_router(combined_router)

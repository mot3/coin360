from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

# from coin.app import coin_router
from market.app import market_router
from rate_limiter import limiter
from settings import settings
from common.schemas import ResponseSchema
from fastapi.exceptions import RequestValidationError
# from pydantic import ValidationError
from pymongo.errors import PyMongoError
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from starlette.exceptions import HTTPException
from error_handler import (http_error_handler, pymongo_error_handler,
                           custom_rate_limit_exceeded_handler, validation_error_http422_error_handler)


app = FastAPI(
    default_response_class=ResponseSchema
)


@app.on_event("startup")
async def startup_event():
    pass
    # write_log(APP_LOGGER, 'info', 'fastapi startup', 'Worker started!')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO add allowed hosts to .env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(
    RateLimitExceeded, custom_rate_limit_exceeded_handler)
app.add_exception_handler(
    RequestValidationError, validation_error_http422_error_handler)
# app.add_exception_handler(
#     ValidationError, validation_error_http422_error_handler)
app.add_exception_handler(PyMongoError, pymongo_error_handler)


# app.include_router(coin_router)
app.include_router(market_router)


@app.get("/", response_class=ORJSONResponse)
@limiter.limit('2/minute')
async def root(request: Request):
    # TODO return main static page here
    return {"message": f"Hello from {settings.APP_NAME}!"}


# route to test connection
@ app.get("/ping", response_class=ORJSONResponse)
async def register_user():
    return {'msg': 'pong'}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)

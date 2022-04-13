from typing import Union
from fastapi import HTTPException, status, Request
from fastapi import Request, Response
from pydantic import ValidationError
from fastapi.responses import ORJSONResponse, JSONResponse
from common.resources import response_string
from fastapi.exceptions import RequestValidationError
from slowapi.errors import RateLimitExceeded
from pymongo.errors import PyMongoError


async def validation_error_http422_error_handler(
        _: Request,
        exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    errors = exc.errors()
    errors[0].update({"code": response_string.VALUE_IS_NOT_VALID})
    return ORJSONResponse(
        {"status": "fail", "errors": errors},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


async def http_error_handler(_: Request, exc: HTTPException) -> ORJSONResponse:
    return ORJSONResponse({"status": "fail", "errors": [{'msg': exc.detail}]}, status_code=exc.status_code)


async def pymongo_error_handler(_: Request, exc: PyMongoError) -> ORJSONResponse:
    return ORJSONResponse({"status": "fail", "errors": [{'args': exc.args,
                                                         'error': 'Database problem occurred.'}]},
                          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom_rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> Response:
    """
    Build a simple JSON response that includes the details of the rate limit
    that was hit. If no limit is hit, the countdown is added to headers.
    """
    detail = exc.detail  # can be used for later(info about limit counts)
    response = ORJSONResponse(
        {"status": "fail", "errors": [{'msg': "Rate limit exceeded"}]}, status_code=429,
    )
    response = request.app.state.limiter._inject_headers(
        response, request.state.view_rate_limit
    )
    return response

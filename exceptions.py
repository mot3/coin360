from fastapi import HTTPException, status

from common.resources import response_string


class AuthenticationError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.headers = {"WWW-Authenticate": "Bearer"}


class ConflictError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = status.HTTP_409_CONFLICT


class ForbiddenError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = status.HTTP_403_FORBIDDEN


class NotAcceptableError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = status.HTTP_406_NOT_ACCEPTABLE


class NotFoundError(HTTPException):
    def __init__(self, detail: str = response_string.NOT_FOUND):
        self.detail = detail
        self.status_code = status.HTTP_404_NOT_FOUND


class BadRequestError(HTTPException):
    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = status.HTTP_400_BAD_REQUEST

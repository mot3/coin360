from typing import Any

from fastapi.responses import ORJSONResponse
from pydantic import BaseModel


class ResponseSchema(ORJSONResponse):
    def __init__(self,
                 content: Any = None,
                 status_code: int = 200,
                 headers: dict = None,
                 media_type: str = None,
                 background=None,
                 status: str = 'ok',
                 errors: dict = []):

        content = {'status': status,
                   'data': content, 'errors': errors}

        super().__init__(content, status_code, headers, media_type, background)


class ResponseModel(BaseModel):
    msg: str

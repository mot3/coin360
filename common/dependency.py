from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field, Extra, root_validator

from db.mongo.engine import Mongo


async def get_db_session():
    async with Mongo() as db:
        yield db


class BaseConfig(BaseModel):
    created_at: datetime = Field(datetime.utcnow())

    @root_validator(pre=True)
    def _set_id(cls, data):
        if '_id' in data:
            id = str(ObjectId(data['_id']))
            data.update({'id': id})
        return data

    class Config:
        extra = Extra.ignore
        use_enum_values = True
        fields = {'id': {'exclude': True}}

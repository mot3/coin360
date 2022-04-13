from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient

from settings import settings


class Mongo:
    _client = None

    def __init__(self, _db: str = settings.APP_NAME) -> None:
        if not Mongo._client:
            Mongo._client = AsyncIOMotorClient("mongodb://localhost:27017")

        self.db = Mongo._client[_db]

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        self._table: AgnosticCollection = self.db[value]

    async def __aenter__(self):
        self.s = await Mongo._client.start_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.s.end_session()
        del self

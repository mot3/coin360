from typing import List
from coin.models import Coin

from db.mongo.engine import Mongo
from common import tables


async def create_coin(db: Mongo, new_coin: Coin):
    db.table = tables.COINS
    res = await db.table.insert_one(new_coin.dict(), session=db.s)

    if res.acknowledged == True:
        return


async def create_coins(db: Mongo, new_coins: List[Coin]):
    db.table = tables.COINS
    res = await db.table.insert_many([coin.dict() for coin in new_coins], session=db.s)

    if res.acknowledged == True:
        return True


async def get_coins(db: Mongo):
    coins: List[Coin] = []

    db.table = tables.COINS
    async for c in db.table.find({}, {'_id': False}, session=db.s):
        coins.append(Coin(**c))

    return coins


async def get_coin(db: Mongo, symbol: str):
    db.table = tables.COINS
    coin = await db.table.find_one({'symbol': symbol}, {'_id': False}, session=db.s)

    if coin:
        return Coin(**coin)


async def update_coin(db: Mongo, symbol: str, coin: Coin):
    db.table = tables.COINS
    res = await db.table.update_one({'symbol': symbol}, {'$set': coin.dict()}, session=db.s)

    if res.modified_count == True:
        return True


async def delete_coin(db: Mongo, symbol: str):
    db.table = tables.COINS
    res = await db.table.delete_one({'symbol': symbol}, session=db.s)

    if res.deleted_count == True:
        return True


async def delete_all_coins(db: Mongo):
    db.table = tables.COINS
    res = await db.table.delete_many({}, session=db.s)

    if res.deleted_count == True:
        return True

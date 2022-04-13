from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter

from coin import crud
from coin.schemas import CoinIn, CoinInList, CoinOut

from db.mongo.engine import Mongo
from common.resources import response_string
from common.schemas import ResponseModel
from common.dependency import get_db_session
from exceptions import NotFoundError

coin_router = APIRouter(
    prefix="/coin",
    tags=["Coin API"])


@coin_router.post("", response_model=ResponseModel)
async def create_coin_ep(new_coin: CoinIn,
                         db: Mongo = Depends(get_db_session)):

    await crud.create_coin(db, new_coin)

    return {'msg': response_string.COIN_CREATED_SUCCESSFULLY}


@coin_router.post("/list", response_model=ResponseModel)
async def create_coins_ep(new_coins: List[CoinInList],
                          db: Mongo = Depends(get_db_session)):

    await crud.create_coins(db, new_coins)

    return {'msg': response_string.COIN_CREATED_SUCCESSFULLY}


@coin_router.get("", response_model=List[CoinOut])
async def get_coin_list_ep(db: Mongo = Depends(get_db_session)):
    return await crud.get_coins(db)


@coin_router.get("/{symbol}", response_model=CoinOut)
async def get_coin_ep(symbol: str, db: Mongo = Depends(get_db_session)):
    coin = await crud.get_coin(db, symbol)

    if coin is None:
        raise NotFoundError(detail=response_string.COIN_NOT_FOUND)

    return coin


@coin_router.put("/{symbol}", response_model=ResponseModel)
async def update_coin_ep(symbol: str,
                         coin: CoinIn,
                         db: Mongo = Depends(get_db_session)):
    res = await crud.update_coin(db, symbol, coin)

    if res is None:
        raise NotFoundError(detail=response_string.COIN_NOT_FOUND)

    return {'msg': response_string.COIN_UPDATED_SUCCESSFULLY}


@coin_router.delete("/{symbol}", response_model=ResponseModel)
async def delete_coin_ep(symbol: str,
                         db: Mongo = Depends(get_db_session)):
    res = await crud.delete_coin(db, symbol)

    if res is None:
        raise NotFoundError(detail=response_string.COIN_NOT_FOUND)

    return {'msg': response_string.COIN_DELETED_SUCCESSFULLY}


@coin_router.delete("", response_model=ResponseModel)
async def delete_all_coins_ep(db: Mongo = Depends(get_db_session)):
    res = await crud.delete_all_coins(db)

    if res is None:
        raise NotFoundError(detail=response_string.COIN_NOT_FOUND)

    return {'msg': response_string.COIN_DELETED_SUCCESSFULLY}

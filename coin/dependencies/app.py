from fastapi.routing import APIRouter

currency_router = APIRouter(
    prefix="/coin",
    tags=["Coin API"])


# @currency_router.get("/list", response_model=List[CurrencySchema], response_class=ORJSONResponse)
# async def get_list(db: Mongo = Depends(get_db_session)):
#     return await crud.get_currencies(db)


# @currency_router.post("/add")
# async def create_currency(new_currency: CurrencySchema,
#                           db: Mongo = Depends(get_db_session)):

#     await crud.create_currency(db, new_currency)

#     return {'code': response_codes.CURRENCY_ADDED_SUCCESS}


# @currency_router.put("/update")
# async def update_coin(updated_currency: CurrencySchema,
#                       db: Mongo = Depends(get_db_session)):
#     currency_id = await crud.get_currency(db, updated_currency.short_name)

#     if currency_id:
#         await crud.update_currency(db, currency_id, updated_currency)

#         return {'code': response_codes.CURRENCY_UPDATED_SUCCESS}

#     raise NotFoundError()


# @currency_router.delete("/delete/{currency_short_name}")
# async def delete_coin(currency_short_name: str,
#                       db: Mongo = Depends(get_db_session)):
#     currency_id = await crud.get_currency(db, currency_short_name)

#     if currency_id:
#         await crud.delete_currency(db, currency_id)
#         return {'code': response_codes.CURRENCY_DELETED_SUCCESS}

#     raise NotFoundError()

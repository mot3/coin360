from typing import List

from fastapi import Depends, WebSocket
from fastapi.routing import APIRouter
from binance import AsyncClient, BinanceSocketManager


market_router = APIRouter(
    prefix="/market",
    tags=["Market API"])


@market_router.websocket_route("/market/websocket_get_markets")
async def websocket_get_positions(websocket: WebSocket):
    await websocket.accept()

    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)

    ts = bm.all_mark_price_socket()

    try:
        async with ts as tscm:
            while True:

                markets = await tscm.recv()

                await websocket.send_json(markets)

    except Exception as e:
        print(e)
        await websocket.close()
        await client.close_connection()

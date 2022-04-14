"""
    BinanceFutures
"""
from binance import AsyncClient, enums

from settings import settings


class CoreApi:
    """
        Communication with binance api
        with Using the pyhton_binance library
    """

    def __init__(self, api_key: str, api_secret: str):
        self._api_key = api_key
        self._api_secret = api_secret
        self._testnet = settings.TESTNET

    async def __aenter__(self):
        self.client: AsyncClient = await AsyncClient.create(self._api_key,
                                                            self._api_secret,
                                                            testnet=self._testnet)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
            Close connection
        """

        await self.client.close_connection()


class OrderApi(CoreApi):
    async def _new_order(self, symbol: str, side: enums, type: enums,
                         quantity: float,  ** params):

        return await self.client.futures_create_order(symbol=symbol, side=side,
                                                      type=type, quantity=quantity,
                                                      **params)

    async def order_limit(self, symbol: str, side: enums, quantity: float, price: int):
        return await self._new_order(symbol, side, enums.FUTURE_ORDER_TYPE_LIMIT,
                                     quantity, price=price, timeInForce=enums.TIME_IN_FORCE_GTC)

    async def order_market(self, symbol: str, side: enums, quantity: float):
        return await self._new_order(symbol, side, enums.FUTURE_ORDER_TYPE_MARKET, quantity)

    async def get_open_orders(self, symbol: str = None, **params):
        return await self.client.futures_get_open_orders(symbol=symbol, **params)

    async def cancel_open_order(self, symbol: str, order_id: int = None, **params):
        return await self.client.futures_cancel_order(symbol=symbol, orderId=order_id, **params)


class ProfileApi(CoreApi):
    async def balance_info(self, asset='USDT', **params):
        res = await self.client.futures_account_balance(**params)
        for balance in res:
            if asset == balance['asset']:
                return balance

    async def position_information(self, symbol: str = None, **params):
        return await self.client.futures_position_information(symbol=symbol, **params)


class CoinApi(CoreApi):
    def __init__(self):
        super().__init__(None, None)

    async def coin_info(self, **params):
        return await self.client.futures_exchange_info(**params)

    async def quantity_precision(self, symbol: str, **params):
        res = await self.coin_info(**params)

        for mark in res['symbols']:
            if mark['symbol'] == symbol.upper():
                return mark['quantityPrecision']

        return None

    async def time(self, **params):
        return await self.client.futures_time(**params)

    async def ticker(self, symbol: str = None, **params):
        return await self.client.futures_symbol_ticker(symbol=symbol, **params)

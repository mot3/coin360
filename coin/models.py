from typing import List

from pydantic import Field

from common.dependency import BaseConfig


class CoinField:
    symbol = Field(max_length=10)
    full_name = Field(max_length=20)
    networks = Field()
    markets = Field()
    description = Field(max_length=200)
    rank = Field(ge=0, le=100000)


class Coin(BaseConfig):
    symbol: str = CoinField.symbol
    full_name: str = CoinField.full_name
    networks: List[str] = CoinField.networks
    markets: List[str] = CoinField.markets
    description: str = CoinField.description
    rank: int = CoinField.rank

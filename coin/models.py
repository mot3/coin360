from typing import List

from pydantic import Field

from common.dependency import BaseConfig


class CoinField:
    symbol = Field(max_length=10)
    name = Field(max_length=20)
    networks = Field([])
    markets = Field([])
    socials = Field([])
    description = Field(max_length=1000)
    rank = Field(0, ge=0, le=100000)


class Coin(BaseConfig):
    symbol: str = CoinField.symbol
    name: str = CoinField.name
    networks: List[str] = CoinField.networks
    markets: List[str] = CoinField.markets
    socials: List[str] = CoinField.socials
    description: str = CoinField.description
    rank: int = CoinField.rank

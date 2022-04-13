from typing import List, Optional

from pydantic import BaseModel

from coin.models import CoinField


class CoinIn(BaseModel):
    symbol: str = CoinField.symbol
    name: str = CoinField.name
    networks: List[str] = CoinField.networks
    markets: List[str] = CoinField.markets
    socials: List[str] = CoinField.socials
    description: str = CoinField.description
    rank: int = CoinField.rank


class CoinOut(CoinIn):
    ...

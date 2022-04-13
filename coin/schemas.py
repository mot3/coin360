from typing import List, Optional

from pydantic import BaseModel

from coin.models import CoinField


class CoinIn(BaseModel):
    symbol: str = CoinField.symbol
    full_name: str = CoinField.full_name
    networks: List[str] = CoinField.networks
    markets: List[str] = CoinField.markets
    description: str = CoinField.description
    rank: int = CoinField.rank


class CoinOut(CoinIn):
    ...

from typing import Any, List, Optional

from pydantic import BaseModel, root_validator, validator

from coin.models import CoinField


class CoinIn(BaseModel):
    symbol: str = CoinField.symbol
    name: str = CoinField.name
    networks: List[str] = CoinField.networks
    markets: List[str] = CoinField.markets
    socials: List[str] = CoinField.socials
    description: str = CoinField.description
    rank: Any = CoinField.rank


class CoinInList(CoinIn):
    @root_validator(pre=True)
    def __post_init__(cls, values: dict) -> None:
        # convert socials to list
        if values.get('socials'):
            values['socials'] = values['socials'].split(',')

        return values


class CoinOut(CoinIn):
    ...

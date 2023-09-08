from typing import List
from pydantic import BaseModel


class Balance(BaseModel):
    time: str
    balance: float
    balance_usd: float


class WalletEntry(BaseModel):
    wallet: str
    last_update_time: str
    current_balance: float
    current_balance_usd: float
    history: List[Balance]


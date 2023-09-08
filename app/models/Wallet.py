from pydantic import BaseModel


class BalanceHistory(BaseModel):
    wallet: str
    time: str
    balance: float
    balance_usd: float


class BalanceCurrent(BaseModel):
    wallet: str
    last_update_time: str
    current_balance: float
    current_balance_usd: float


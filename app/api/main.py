from typing import List
from fastapi import FastAPI
from datetime import datetime

from app.utils import price
from app.eth import eth_client
from app.models.Wallet import BalanceHistory, BalanceCurrent
from app.crud.Wallet import put_crv_entry, get_crv_history

app = FastAPI()


@app.put("/wallet/{wallet_address}", response_model=BalanceCurrent)
async def update_wallet_balance(wallet_address: str):
    balance = await eth_client.crv_balanceOf(wallet_address)
    price_usd = price.get_crv_price()
    price_total = balance * price_usd

    current_balance = BalanceCurrent(
        wallet=wallet_address,
        last_update_time=str(datetime.now()),
        current_balance=float(balance),
        current_balance_usd=float(price_total)
    )
    put_crv_entry(current_balance)

    return current_balance


@app.get("/wallet/{wallet_address}", response_model=List[BalanceHistory])
async def wallet_balance_history(wallet_address: str, limit: int = 20, skip: int = 0):
    return get_crv_history(wallet_address, limit, skip)

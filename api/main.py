from typing import List
from fastapi import FastAPI
from datetime import datetime

from utils import price
from eth import eth_client
from models.Wallet import Balance
from crud.Wallet import put_crv_entry, get_crv_history

app = FastAPI()


@app.put("/wallet/{wallet_address}", response_model=Balance)
async def update_wallet_entry(wallet_address: str):
    balance = await eth_client.crv_balanceOf(wallet_address)
    price_usd = price.get_crv_price()
    price_total = balance * price_usd

    current_balance = Balance(
        time=str(datetime.now()),
        balance=float(balance),
        balance_usd=float(price_total)
    )
    put_crv_entry(wallet_address, current_balance)

    return current_balance


@app.get("/wallet/{wallet_address}", response_model=List[Balance])
async def get_wallet_info(wallet_address: str):
    return get_crv_history(wallet_address)

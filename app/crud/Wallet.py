from typing import List
from app.db.mongo_db import db_crv_current, db_crv_history
from app.models.Wallet import BalanceCurrent, BalanceHistory


def put_crv_entry(current_balance: BalanceCurrent):
    wallet_address = current_balance.wallet
    db_crv_current.replace_one({"wallet": wallet_address}, current_balance.model_dump(), True)

    new_entry = BalanceHistory(
        wallet=wallet_address,
        time=current_balance.last_update_time,
        balance=current_balance.current_balance,
        balance_usd=current_balance.current_balance_usd,
    )
    db_crv_history.insert_one(new_entry.model_dump())


def get_crv_history(wallet_address: str, limit: int, skip: int):
    items = db_crv_history.find({"wallet": wallet_address}).limit(limit).skip(skip)

    result_list: List[BalanceHistory] = []
    for item in items:
        balance_history_entry = BalanceHistory(
            wallet=wallet_address,
            time=item['time'],
            balance=item['balance'],
            balance_usd=item['balance_usd'],
        )
        result_list.append(balance_history_entry)
    return result_list

from db.mongo_db import collection_crv
from models.Wallet import Balance, WalletEntry


def put_crv_entry(wallet_address: str, current_balance: Balance):
    new_entry = WalletEntry(
        wallet=wallet_address,
        last_update_time=current_balance.time,
        current_balance=current_balance.balance,
        current_balance_usd=current_balance.balance_usd,
        history=[]
    )

    existing_entry = collection_crv.find_one({"wallet": wallet_address})
    if existing_entry is not None:
        new_entry.history = existing_entry['history']
    new_entry.history.append(current_balance)

    collection_crv.replace_one({"wallet": wallet_address}, new_entry.model_dump(), True)


def get_crv_history(wallet_address: str):
    item = collection_crv.find_one({"wallet": wallet_address})
    if item is None:
        return []
    return item['history']

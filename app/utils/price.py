from decimal import Decimal
import requests

from app.utils import constants

PRICE_URL = ('https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses='
             + constants.CRV_TOKEN_ADDRESS + '&vs_currencies=usd')


def get_crv_price():
    response = requests.get(PRICE_URL)
    price = response.json()[constants.CRV_TOKEN_ADDRESS.lower()]['usd']
    return Decimal(price)

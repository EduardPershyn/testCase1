from web3 import Web3, AsyncWeb3
from eth_abi import abi

from app.utils import constants

INFURA_ENDPOINT = "https://mainnet.infura.io/v3/024248831c8f4b5b9c280e2af82c2752"

w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(INFURA_ENDPOINT))


async def crv_balanceOf(wallet_address: str):
    selector = '0x70a08231'  # balanceOf(address) selector
    calldata = selector + wallet_address[2:].rjust(64, '0')

    response = await w3.eth.call({'to': constants.CRV_TOKEN_ADDRESS, 'data': calldata})
    wei_units = abi.decode(['uint256'], response)[0]
    eth_units = Web3.from_wei(wei_units, 'ether')

    return eth_units

Test Case 1
----------

To execute:
```
docker-compose up
```

http://127.0.0.1:8000/docs

GET http://127.0.0.1:8000/wallet/0x7a16ff8270133f063aab6c9977183d9e72835428

PUT http://127.0.0.1:8000/wallet/0x7a16ff8270133f063aab6c9977183d9e72835428


Task
----------
You need to build python api with FastAPI framework to get current balance (token amount and
usd amount) of CRV mainnet token for specific wallet:
https://etherscan.io/address/0xD533a949740bb3306d119CC777fa900bA034cd52

1. First endpoint should return current wallet balances for given param: wallet=0x...After
fetching balance, app should save next data to mongoDB:wallet, last update time,
current balance, current balance usd, history of balances (isotimestamp-value) for token
and usd balances.

2. Second endpoint should return existing history from mongodb for given param:
wallet=0x...


Please DO NOT use etherscan api to get token balance, you need to get it from blockchain
node with web3py (or other methods you would like).

Final result must have a docker-compose file and be ready for testing with only one command:
docker-compose up.
Wallet for testing: 0x7a16ff8270133f063aab6c9977183d9e72835428
Sources:

● Web3py – https://web3py.readthedocs.io/en/stable/

● CoinGecko Pricing API – https://www.coingecko.com/ru/api/documentation
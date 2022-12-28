import os

from binance.client import Client

# init
btest= True
if not btest :
    api_key = os.environ.get('binance_api')
    api_secret = os.environ.get('binance_secret')
else:
    api_key = 'KgBi3o5IpO21XMA6W7Ocbrtq3QDzELu6qWhply1ElK6QNuo8Nwl4kh78jyFNE9kb'
    api_secret ='8qRNW4VhHl6Gb5EW2liIyHkXxIy1n8gQOlOeLn2W7dj1zSiCvdkE4h7b7SubIIpW'

client = Client(api_key, api_secret)
if btest : 
    client.API_URL = 'https://testnet.binance.vision/api'

## main

# get balances for all assets & some account information
print(client.get_account())

# get balance for a specific asset only (BTC)
print(client.get_asset_balance(asset='BTC'))

# get balances for futures account
if not btest : 
    print(client.futures_account_balance())

# get balances for margin account
# will raise an exception if margin account is not activated
#print(client.get_margin_account())

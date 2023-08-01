
import alpaca_toolkit as at

# Define the Alpaca API key and secret
api_key = "<YOUR_ALPACA_API_KEY>"
api_secret = "<YOUR_ALPACA_API_SECRET>"

# Initialize the Alpaca toolkit
toolkit = at.AlpacaToolkit(api_key, api_secret)

# Use the toolkit
account = toolkit.get_account()
print(account)

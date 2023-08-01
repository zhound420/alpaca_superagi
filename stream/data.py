import alpaca_trade_api as tradeapi

class StreamAPI:
    def __init__(self, api_key, api_secret, base_url, data_feed='iex'):
        self.stream = tradeapi.stream.Stream(api_key, api_secret, base_url, data_feed)

    def subscribe_trades(self, func, symbol):
        self.stream.subscribe_trades(func, symbol)

    def subscribe_quotes(self, func, symbol):
        self.stream.subscribe_quotes(func, symbol)

    def subscribe_bars(self, func, symbol):
        self.stream.subscribe_bars(func, symbol)

    def run(self):
        self.stream.run()

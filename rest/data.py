import alpaca_trade_api as tradeapi

class DataAPI:
    def __init__(self, api_key, api_secret, base_url):
        self.api = tradeapi.REST(api_key, api_secret, base_url)

    def get_bars(self, symbol, timeframe, start, end, adjustment='raw'):
        return self.api.get_bars(symbol, timeframe, start, end, adjustment).df

    def get_quotes(self, symbol, start, end):
        return self.api.get_quotes(symbol, start, end).df

    def get_trades(self, symbol, start, end):
        return self.api.get_trades(symbol, start, end).df

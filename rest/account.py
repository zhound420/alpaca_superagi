import alpaca_trade_api as tradeapi

class AccountAPI:
    def __init__(self, api_key, api_secret, base_url):
        self.api = tradeapi.REST(api_key, api_secret, base_url)

    def get_account(self):
        return self.api.get_account()

    def list_positions(self):
        return self.api.list_positions()

    def submit_order(self, symbol, qty, side, type, time_in_force):
        return self.api.submit_order(symbol, qty, side, type, time_in_force)

    def cancel_order(self, order_id):
        return self.api.cancel_order(order_id)

    def list_orders(self, status=None):
        return self.api.list_orders(status)

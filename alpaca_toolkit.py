from typing import List
from superagi.tools.base_tool import BaseToolkit
from alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from alpaca_get_positions_tool import AlpacaGetPositionsTool
from alpaca_monitor_tool import AlpacaMonitorTool

class AlpacaToolkit(BaseToolkit):
    name = "Alpaca Toolkit"
    description = "Toolkit for interacting with Alpaca API"

    def get_tools(self):
        return [AlpacaGetAccountInformationTool(), AlpacaGetPositionsTool(), AlpacaMonitorTool()]

    def get_env_keys(self) -> List[str]:
        return [
        "APCA_API_KEY_ID",
        "APCA_API_SECRET_KEY",
        "APCA_PAPER"
        ]



    def get_order_by_client_order_id(self, client_order_id):
        try:
            order = self.alpaca.get_order_by_client_order_id(client_order_id)
            return order._raw
        except Exception as e:
            print(f'Error getting order by client order ID: {e}')
            return None


    def get_position(self, symbol):
        try:
            position = self.alpaca.get_position(symbol)
            return position._raw
        except Exception as e:
            print(f'Error getting position: {e}')
            return None


    def list_assets(self, status=None, asset_class=None):
        try:
            assets = self.alpaca.list_assets(status=status, asset_class=asset_class)
            return [asset._raw for asset in assets]
        except Exception as e:
            print(f'Error listing assets: {e}')
            return None


    def get_asset(self, symbol):
        try:
            asset = self.alpaca.get_asset(symbol)
            return asset._raw
        except Exception as e:
            print(f'Error getting asset: {e}')
            return None


    def get_calendar(self, start=None, end=None):
        try:
            calendar = self.alpaca.get_calendar(start=start, end=end)
            return [cal._raw for cal in calendar]
        except Exception as e:
            print(f'Error getting calendar: {e}')
            return None


    def get_portfolio_history(self, date_start=None, date_end=None, period=None, timeframe=None, extended_hours=None):
        try:
            portfolio_history = self.alpaca.get_portfolio_history(date_start=date_start, date_end=date_end, period=period, timeframe=timeframe, extended_hours=extended_hours)
            return portfolio_history._raw
        except Exception as e:
            print(f'Error getting portfolio history: {e}')
            return None

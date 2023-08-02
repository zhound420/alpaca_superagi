from .alpaca_get_asset_info_tool import Tool as AlpacaGet_asset_infoTool
from .alpaca_get_all_assets_tool import Tool as AlpacaGet_all_assetsTool
from .alpaca_update_order_tool import Tool as AlpacaUpdate_orderTool
from .alpaca_cancel_order_tool import Tool as AlpacaCancel_orderTool
from .alpaca_cancel_all_orders_tool import Tool as AlpacaCancel_all_ordersTool
from .alpaca_get_all_orders_tool import Tool as AlpacaGet_all_ordersTool
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


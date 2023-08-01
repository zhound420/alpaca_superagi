
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from .account_tool import AccountTool
from .positions_tool import PositionsTool
from .orders_tool import OrdersTool
from .assets_tool import AssetsTool

class AlpacaToolkit(BaseToolkit):
    name: str = "Alpaca Toolkit"
    description: str = "Toolkit for interacting with Alpaca API"

    def get_tools(self) -> List[BaseTool]:
        return [AccountTool(), PositionsTool(), OrdersTool(), AssetsTool()]

    def get_env_keys(self) -> List[str]:
        return ["APCA_API_KEY_ID", "APCA_API_SECRET_KEY", "APCA_API_BASE_URL"]

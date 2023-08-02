
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class ToolInput(BaseModel):
    pass

class Tool(BaseTool):
    name: str = "Tool"
    args_schema: Type[BaseModel] = ToolInput
    description: str = "Description of the tool"

    def _execute(self):
        pass

from typing import Callable

from pydantic import BaseModel

from ai2sql.react import AI2SQL_PROMPT
from ai2sql.tools import db_metadata


class Tool(BaseModel):
    name: str
    description: str
    func: Callable[[str], str]


class ReActAgent:
    def __init__(self):
        self.tools = [
            Tool(
                name="TableInfoByCata",
                func=db_metadata.tables_info,
                description="查询并返回输入类别下所有表的信息.输入的可选项为[公司管理, 股票行情]",
            ),
            Tool(
                name="TableColumnsByTable",
                func=db_metadata.table_columns,
                description="查询并返回Table所有列的信息.输入的内容为Table的名称",
            ),
        ]
        self.prompt = AI2SQL_PROMPT

    @property
    def thought_prefix(self) -> str:
        return "Thought: "

    @property
    def action_prefix(self) -> str:
        return "Action: "

    @property
    def action_input_prefix(self) -> str:
        return "Action Input: "

    @property
    def observation_prefix(self) -> str:
        return "Observation: "

    @property
    def final_answer_prefix(self) -> str:
        return "Final Answer: "

    def _tools_description(self):
        tools_description = ""
        for tool in self.tools:
            tools_description += f"{tool.name}: {tool.description}\n"
        return tools_description[:-1]

    def _tools_name(self):
        tools_name = ""
        for tool in self.tools:
            tools_name += f"{tool.name},"
        return tools_name[:-1]

    def _format_prompt(self):
        self.prompt = self.prompt.format(
            tools_description=self._tools_description(), tools_name=self._tools_name()
        )

    def run(self):
        self._format_prompt()

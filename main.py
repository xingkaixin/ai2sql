from ai2sql.chat_model import ChatOpenAI
from ai2sql.core import load_skill
from ai2sql.react import ReActAgent
from ai2sql.tools import Tool, table_columns, tables_info


def main():
    # chat_config = load_skill("AI2Sql")
    chat_config = load_skill("AI2Sql")

    llm = ChatOpenAI(
        **chat_config.completion.dict(exclude={"stop"}),
    )

    tools = [
        Tool(
            name="TableInfoByCata",
            func=tables_info,
            description="查询并返回输入类别下所有表的信息.输入的可选项为[公司管理, 股票行情]",
        ),
        Tool(
            name="TableColumnsByTable",
            func=table_columns,
            description="查询并返回Table所有列的信息.输入的内容为Table的名称",
        ),
    ]

    agent = ReActAgent(tools, llm, chat_config.prompt)
    question = "列出上市公司最新股本"
    answer = agent.run(question)

    print(answer)


if __name__ == "__main__":
    main()

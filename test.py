from ai2sql.chat_model import ChatOpenAI
from ai2sql.core import load_skill
from ai2sql.react import ReActAgent
from ai2sql.schemas.message import AIMessage, SystemMessage, UserMessage
from ai2sql.schemas.template import SystemMessageTemplate, UserMessageTemplate


def main():
    sys_template = "a {a} {c}"
    user_template = "b {d}"
    sys = SystemMessageTemplate.from_template(sys_template)
    user = UserMessageTemplate.from_template(user_template)

    sys_msg = SystemMessage(content="system message test")
    sys_prompt = sys.format_prompt(a="aa", c="ccc")

    chat_config = load_skill("AI2Sql")

    agent = ReActAgent(prompt=chat_config.prompt)
    agent.run()
    sys_msg = SystemMessage(content=agent.prompt)
    usr_msg = UserMessage(content="查询上市公司最新股本")

    chat = ChatOpenAI(
        **chat_config.completion.dict(exclude={"stop"}),
    )

    answer = chat([sys_msg, usr_msg], stop=chat_config.completion.stop)

    print(answer)


if __name__ == "__main__":
    main()

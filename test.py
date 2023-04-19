from ai2sql.chat_model import ChatOpenAI
from ai2sql.core import load_skill
from ai2sql.react import ReActAgent
from ai2sql.schemas.message import AIMessage, SystemMessage, UserMessage
from ai2sql.schemas.template import SystemMessageTemplate, UserMessageTemplate

sys_template = "a {a} {c}"
user_template = "b {d}"
sys = SystemMessageTemplate.from_template(sys_template)
user = UserMessageTemplate.from_template(user_template)


sys_msg = SystemMessage(content="system message test")
sys_prompt = sys.format_prompt(a="aa", c="ccc")

chat = ChatOpenAI()
# msg = chat([sys_msg])z
# print(msg)

ai2sql_config = load_skill("AI2Sql")


agent = ReActAgent(prompt=ai2sql_config["prompt"])
agent.run()
sys_msg = SystemMessage(content=agent.prompt)
usr_msg = UserMessage(content="查询公司所有上市的公司上市代码，公司名称、董秘姓名")

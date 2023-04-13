from ai2sql.chat_model import ChatOpenAI
from ai2sql.react import ReActAgent
from ai2sql.schemas.message import SystemMessage
from ai2sql.schemas.template import SystemMessageTemplate, UserMessageTemplate

sys_template = "a {a} {c}"
user_template = "b {d}"
sys = SystemMessageTemplate.from_template(sys_template)
user = UserMessageTemplate.from_template(user_template)


sys_msg = SystemMessage(content="system message test")
sys_prompt = sys.format_prompt(a="aa", c="ccc")

chat = ChatOpenAI()
msg = chat([sys_msg])
print(msg)
agent = ReActAgent()
agent.run()
print(agent.prompt)

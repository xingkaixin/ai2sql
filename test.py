from ai2sql.chat_model import ChatOpenAI
from ai2sql.schemas.message import SystemMessage
from ai2sql.schemas.template import ChatPromptTemplate, SystemTemplate, UserTemplate

sys_template = "a {a} {c}"
user_template = "b {d}"
sys = SystemTemplate.from_template(sys_template)
user = UserTemplate.from_template(user_template)
chat = ChatPromptTemplate.from_messages(messages=[sys, user])


sys_msg = SystemMessage(content="system message test")

chat_prompt = chat.format_prompt(a="aa", d="bb", c="ccc").to_messages()


c = ChatOpenAI()
msg = c(sys_msg)

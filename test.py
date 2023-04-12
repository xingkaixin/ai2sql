from schemas.message import SystemMessage
from schemas.template import ChatPromptTemplate, SystemTemplate, UserTemplate

sys_template = "a {a} {c}"
user_template = "b {d}"
sys = SystemTemplate.from_template(sys_template)
user = UserTemplate.from_template(user_template)
chat = ChatPromptTemplate.from_messages(messages=[sys, user])
print(chat.format_prompt(a="aa", d="bb", c="ccc").to_messages())


sys_msg = SystemMessage(content="a bc")
print(sys_msg)

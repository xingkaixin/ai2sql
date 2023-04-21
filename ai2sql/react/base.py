from ai2sql.chat_model import BaseChatModel
from ai2sql.schemas.message import AIMessage, SystemMessage, UserMessage
from ai2sql.tools import Tool


class ReActAgent:
    def __init__(self, tools: list[Tool], llm: BaseChatModel, prompt: str):
        self.tools = tools
        self.prompt = prompt
        self.llm = llm
        self.max_turns = 5
        self.current_turn = 0

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

    @property
    def tools_description(self) -> str:
        return "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])

    @property
    def tools_name(self) -> str:
        return ",".join([tool.name for tool in self.tools])

    def _format_prompt(self) -> None:
        return self.prompt.format(tools_description=self.tools_description, tools_name=self.tools_name)

    def run(self, question: str):
        sys_msg = SystemMessage(content=self._format_prompt())
        usr_msg = UserMessage(content=f"Question: {question}")
        chat_msgs = [sys_msg, usr_msg]
        answer = self.llm(messages=chat_msgs, stop=[self.observation_prefix])

        while self.action_prefix in answer:
            if self.current_turn > self.max_turns:
                break
            self.current_turn += 1

            print(f"Step {self.current_turn}:\n{answer}")

            action_tool = self._find_tool_by_name(answer.split(self.action_prefix)[1].split("\n")[0])
            action_observation = action_tool.func(answer.split(self.action_input_prefix)[1].split("\n")[0])
            chat_msgs.append(AIMessage(content=f"{self.observation_prefix}{action_observation}"))
            answer = self.llm(messages=chat_msgs, stop=[self.observation_prefix])

            print("answer:", answer)

        if self.final_answer_prefix in answer:
            return answer.split(self.final_answer_prefix)[1]
        return answer

    def _find_tool_by_name(self, tool_name: str) -> Tool:
        return [tool for tool in self.tools if tool.name in tool_name][0]

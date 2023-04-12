from rich.console import Console

from action import TableColumn, TableInfo
from bot import GPTBot
from prompt.pre_prompt import sys_prompt
from prompt.prompt_message import ChatRole, PromptMessage
from utils import logger

console = Console()


def main():
    i = 0
    bot = GPTBot()
    messages = []
    question = "公司董秘信息"
    console.print(
        f"[bold green]Question:[/bold green] [green]{question}[/green]"
    )  # noqa E501
    logger.info(f"Question: {question}")
    messages.append(sys_prompt.message)
    messages.append(PromptMessage(ChatRole.user, question).message)
    output = bot.ask(messages)
    logger.info(f"{output=}")

    while "Action" in output:
        i += 1
        console.print(f"[bold yellow]AI Action {i}[/bold yellow]")
        console.print(f"[yellow]{output}[/yellow]")
        action = output.split("Action: ")[1].split("\n")[0]
        action_input = output.split("Action Input: ")[1].split("\n")[0]
        if (
            "TableInfoByCata" not in action
            and "TableColumnsByTable" not in action  # noqa
        ):
            break
        logger.info(f"{action=}")
        logger.info(f"{action_input=}")

        if "TableInfoByCata" in action:
            response = TableInfo(action_input).answer()
        if "TableColumnsByTable" in action:
            response = TableColumn(action_input).answer()
        console.print(
            f"[bold red]Observation:[/bold red] [red]{response}[/red]"
        )  # noqa E501

        messages.append(PromptMessage(ChatRole.assistant, output).message)
        messages.append(
            PromptMessage(
                ChatRole.assistant, f"Observation: {response}"
            ).message  # noqa
        )
        output = bot.ask(messages)
        logger.info(f"{output=}")
    try:
        final_answer = output.split("Final Answer: ")[1].split("\n")[0]
    except Exception:
        logger.exception("get final answer failed")
        final_answer = output
    logger.success(f"{question=}")
    logger.success(f"{final_answer=}")
    console.print(
        f"[bold yellow]Final Answer:[/bold yellow] [yellow]{final_answer}[/yellow]"  # noqa E501
    )


if __name__ == "__main__":
    main()

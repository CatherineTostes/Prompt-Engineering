from rich.console import Console
from rich.text import Text


def print_llm_result(label, response):
    """
    Args:
        label (str): Identificador do cenário (ex.: professor, msg1).
        response: Objeto de mensagem do LangChain (ex.: AIMessage).
    """

    console = Console()

    console.print(Text(f"Cenário: {label}", style="bold blue"))

    text = getattr(response, "content", response)
    console.print(Text("Assistant Response:", style="bold green"))
    console.print(Text(str(text), style="bold green"))

    usage = (response.response_metadata or {}).get("token_usage") or {}

    def print_metric(name: str, value):
        line = Text(f"{name}: ", style="bold white")
        line.append(str(value), style="bright_black")
        console.print(line)

    print_metric("Input Tokens", usage.get("prompt_tokens", "—"))
    print_metric("Output Tokens", usage.get("completion_tokens", "—"))
    print_metric("Total Tokens", usage.get("total_tokens", "—"))
    for key in ("total_cost", "prompt_cost", "completion_cost"):
        if key in usage:
            print_metric(key, f"{usage[key]:.6f}")
    console.print(f"[yellow]{'-' * 50}[/yellow]")

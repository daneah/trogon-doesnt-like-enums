from enum import Enum
from typing import Optional

import typer
from trogon import Trogon
from typing_extensions import Annotated
from typer.main import get_group


app = typer.Typer()


class PowerpuffGirls(str, Enum):
    BLOSSOM = "Blossom"
    BUBBLES = "Bubbles"
    BUTTERCUP = "Buttercup"


@app.command()
def hello_with_option_with_default(name: Annotated[PowerpuffGirls, typer.Option("--name", "-n")] = PowerpuffGirls.BLOSSOM):
    """Trogon doesn't like this one"""
    print(f"Hello, {name.value}!")


@app.command()
def hello_with_option_without_default(name: Annotated[Optional[PowerpuffGirls], typer.Option("--name", "-n")] = None):
    """Trogon likes this one fine"""
    print(f"Hello, {name.value}!")


@app.command()
def hello_with_argument(name: Annotated[PowerpuffGirls, typer.Argument()]):
    """Trogon likes this one fine"""
    print(f"Hello, {name.value}!")


@app.command()
def tui(context: typer.Context):
    Trogon(get_group(app), click_context=context).run()


if __name__ == "__main__":
    app()

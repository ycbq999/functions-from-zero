#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div, power
import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers

    Example:
    ./calCLI.py add 1 2
    """
    # use colored output to print the result
    click.echo(click.style(f"{add(a, b)}", fg="green"))


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_command(a, b):
    """Subtract two numbers

    Example:
    ./calCLI.py sub 1 2
    """
    click.echo(click.style(f"{sub(a, b)}", fg="green"))


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_command(a, b):
    """Multiply two numbers

    Example:
    ./calCLI.py mul 1 2
    """
    click.echo(click.style(f"{mul(a, b)}", fg="green"))


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_command(a, b):
    """Divide two numbers

    Example:
    ./calCLI.py div 1 2
    """
    click.echo(click.style(f"{div(a, b)}", fg="green"))


@cli.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_command(x, y):
    """Power of a number

    Example:
    ./calCLI.py power 1 2
    """
    click.echo(click.style(f"{power(x, y)}", fg="green"))


if __name__ == "__main__":
    cli()

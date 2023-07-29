#!/usr/bin/env python3

from mylib.logistics import (
    distance_between_two_points,
    cities_list,
    get_coordinates,
    travel_time,
)
import click


@click.group()
def cli():
    """
    Logistics command-line
    """


@cli.command("cities")
def cities():
    """
    List cities

    Example:
    ./python logisticsCLI.py cities
    """
    # use the cities_list function to print the list of cities with colors
    click.echo(click.style("The list of cities are:", fg="green"))
    for city in cities_list():
        click.echo(click.style(city, fg="blue"))


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """
    Calculate the distance between two cities

    Example:
    ./python logisticsCLI.py distance "New York" "Los Angeles"
    """
    # use the distance_between_two_points function to calculate the distance between two cities
    click.echo(click.style(f"The distance between {city1} and {city2} is:", fg="green"))
    click.echo(
        click.style(
            f"{distance_between_two_points(get_coordinates(city1), get_coordinates(city2))} miles",
            fg="blue",
        )
    )


# build a click command to estimate the travel time between two cities by car
@cli.command("travel")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=60, help="The speed of the car")
def travel(city1, city2, speed):
    """
    Estimate the travel time between two cities by car

    Example:
    ./python logisticsCLI.py travel "New York" "Los Angeles" --speed 80
    """
    # use the travel_time function to estimate the travel time between two cities by car
    click.echo(
        click.style(
            f"The travel time between {city1} and {city2} by car is:", fg="green"
        )
    )
    click.echo(click.style(f"{travel_time(city1, city2, speed)} hours", fg="blue"))


# invoke the click command
if __name__ == "__main__":
    cli()

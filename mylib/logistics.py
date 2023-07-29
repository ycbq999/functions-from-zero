"""
This module deals with logistics and calculate distances between two points
and the time it takes to travel between two points and other logistics related questions for a given speed
"""

from geopy import distance


# build a list of 10 cities in the USA with their coordinates
# make a list of tuples of the cities and their coordinates
CITIES = [
    ("New York", (40.7128, 74.0060)),
    ("Los Angeles", (34.0522, 118.2437)),
    ("Chicago", (41.8781, 87.6298)),
    ("Houston", (29.7604, 95.3698)),
    ("Phoenix", (33.4484, 112.0740)),
    ("Philadelphia", (39.9526, 75.1652)),
    ("San Antonio", (29.4241, 98.4936)),
    ("San Diego", (32.7157, 117.1611)),
    ("Dallas", (32.7767, 96.7970)),
    ("San Jose", (37.3382, 121.8863)),
    ("San Francisco", (37.7749, 122.4194)),
    ("El Paso", (31.7619, 106.4850)),
]


def distance_between_two_points(point1, point2):
    """
    This function calculates the distance between two points
    """
    return distance.distance(point1, point2).miles


# retrun the coordinates of a city
def get_coordinates(city):
    """
    Return the coordinates of a city
    """
    for city_name, coordinates in CITIES:
        if city_name == city:
            return coordinates


# print(distance_between_two_points((41.49008, -71.312796), (41.499498, -81.695391)))


# calculate the total distance between a list of cities
def cities_list():
    """
    Return the list of cities
    """

    return [city[0] for city in CITIES]


# estimate the travel time between two cities by car
# assume the speed is 60 miles per hour
def travel_time(city1, city2, speed=60):
    """
    Estimate the travel time between two cities by car
    Assume the default speed is 60 miles per hour
    """
    return (
        distance_between_two_points(get_coordinates(city1), get_coordinates(city2))
        / speed
    )


# print(distance_between_two_points(CITIES[0][1], CITIES[1][1]))
# print_cities()

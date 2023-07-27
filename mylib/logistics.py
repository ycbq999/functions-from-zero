"""
This module deals with logistics and calculate distances between two points
and the time it takes to travel between two points and other logistics related questions for a given speed
"""

from geopy import distance


# build a list of 10 cities in the USA with their coordinates
# make a list of tuples of the cities and their coordinates
cities = [
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
]


def distance_between_two_points(point1, point2):
    """
    This function calculates the distance between two points
    """
    return distance.distance(point1, point2).miles


# print(distance_between_two_points((41.49008, -71.312796), (41.499498, -81.695391)))

# build a function that finds the coordinates of a city given its name
def find_coordinates(city):
    """
    This function finds the coordinates of a city
    """
    return city.latitude, city.longitude


# calculate the total distance between a list of cities
def total_distance(cities):
    """
    This function calculates the total distance between a list of cities
    """
    total_distance = 0
    for i in range(len(cities) - 1):
        total_distance += distance_between_two_points(cities[i], cities[i + 1])
    return total_distance

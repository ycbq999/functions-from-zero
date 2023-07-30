from mylib.logistics import (
    distance_between_two_points,
    cities_list,
    CITIES,
    travel_time,
)
from fastapi.testclient import TestClient

from main import app
import pytest


def test_distance_between_two_points():
    """
    This function tests the distance_between_two_points function
    """
    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 2450.9503446683375


def test_cities_list():
    """
    This function tests the print_cities function
    """
    assert "New York" in cities_list()


# build a test for the travel_time function
def test_travel_time():
    """
    This function tests the travel_time function
    """
    assert travel_time("New York", "Los Angeles", 60) == 40.84917241113896


#### Web Application Testing ####


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}


# build a test for the cities endpoint
def test_cities(client):
    response = client.get("/cities")
    assert response.status_code == 200
    assert response.json() == {"cities": cities_list()}
    assert "New York" in response.json()["cities"]
    assert "Los Angeles" in response.json()["cities"]
    assert "Chicago" in response.json()["cities"]
    assert "Houston" in response.json()["cities"]
    assert "Phoenix" in response.json()["cities"]
    assert "Philadelphia" in response.json()["cities"]
    assert "San Antonio" in response.json()["cities"]
    assert "San Diego" in response.json()["cities"]


# build a test for the distance endpoint
def test_distance(client):
    response = client.post(
        "/distance",
        json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert response.json() == {"distance": 2450.9503446683375}


# build a test the travel time between two cities by car
def test_travel_time(client):
    response = client.post(
        "/travel",
        json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert response.json() == {"travel_time": "41 hours"}

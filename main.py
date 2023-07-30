from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import (
    distance_between_two_points,
    cities_list,
    get_coordinates,
    travel_time,
)

from mylib.wiki import get_wiki_keywords


app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """List cities with GET HTTP Method
    Return back a list of cities that are available to get further information about"""

    return {"cities": cities_list()}


# build a post method to calculate the travel time between two cities by car
@app.post("/travel")
async def travel(city1: City, city2: City, speed: float = 60.0):
    """Estimate the travel time between two cities by car with POST HTTP Method
    Return back the travel time between two cities"""

    hours = travel_time(city1.name, city2.name, speed)
    return {"travel_time": f"{int(hours)} hours"}


# build a post method to get the distance between two cities
@app.post("/distance")
async def distance(city1: City, city2: City):
    """Calculate the distance between two cities with POST HTTP Method
    Return back the distance between two cities"""

    return {
        "distance": distance_between_two_points(
            get_coordinates(city1.name), get_coordinates(city2.name)
        )
    }


@app.post("/keywords")
async def keywords(city: City):
    """Get the keywords from a wikipedia page with POST HTTP Method
    Return back the keywords from a wikipedia page"""

    return {"keywords": get_wiki_keywords(city.name)}




if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")

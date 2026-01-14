import asyncio
import random
import time
from http.client import HTTPException

from app.movies.db import dict_movies
from app.movies.schemas import MovieCreate, MovieUpdate, MovieReplace


async def get_movie_from_db(id : int):
    await asyncio.sleep(0.2 + (random.random() / 10))
    movie = dict_movies.get(id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

async def get_movies_from_db(limit : int):
    await asyncio.sleep(0.2 + (random.random() / 10))
    list_movies = []
    for i in range(1, limit + 1):
        movie = dict_movies.get(i)
        if movie is not None:
            list_movies.append({"id" : i, **movie})
    return list_movies

def len_db():
    return len(dict_movies)


async def set_movie_to_db(model : MovieCreate):
    await asyncio.sleep(0.2 + (random.random() / 10))
    id = len_db() + 1
    dict_movie = {"movie" : model.movie, "year" : model.year}
    dict_movies[id] = dict_movie
    return id, dict_movie

async def delete_movie_from_db(id : int):
    await asyncio.sleep(0.2 + (random.random() / 10))
    if dict_movies.get(id) is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie = dict_movies.pop(id)
    return movie

async def update_movie_from_db(id : int, model : MovieReplace):
    await asyncio.sleep(0.2 + (random.random() / 10))
    dict_movie = {"movie": model.movie, "year": model.year}
    dict_movies[id] = dict_movie
    return dict_movie

async def update_part_movie_from_db(id : int, model : MovieUpdate):
    await asyncio.sleep(0.2 + (random.random() / 10))

    dict_movie = dict_movies.get(id)
    if dict_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    if model.movie is not None:
        dict_movie["movie"] = model.movie
    if model.year is not None:
        dict_movie["year"] = model.year

    dict_movies[id] = dict_movie
    return dict_movie


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# DAY 1. Just for experiments
#
# | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sync_get_movie_from_db(id : int):
    time.sleep(0.2 + (random.random() / 10))
    return dict_movies.get(id)

async def create_log(id : int):
    await asyncio.sleep(2)
    print(f"A search was made for a movie with such an ID: {id}")
import asyncio
import random
import time
from app.movies.db import dict_movies


async def get_movie_from_db(id : int):
    await asyncio.sleep(0.2 + (random.random() / 10))
    return dict_movies.get(id)

def sync_get_movie_from_db(id : int):
    time.sleep(0.2 + (random.random() / 10))
    return dict_movies.get(id)

async def create_log(id : int):
    await asyncio.sleep(2)
    print(f"A search was made for a movie with such an ID: {id}")
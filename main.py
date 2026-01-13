from fastapi import FastAPI, BackgroundTasks
import asyncio
import random
import time

app = FastAPI()

dict_movies = {
    # id : value
    1 : "Terminator",
    2 : "Harry Potter",
    3 : "Blade Runner",
    4 : "Godfather",
    5 : "Fight Club"
}

async def get_movie_from_db(id : int):
    await asyncio.sleep(0.2 + (random.random() / 10))
    return dict_movies.get(id)

def sync_get_movie_from_db(id : int):
    time.sleep(0.2 + (random.random() / 10))
    return dict_movies.get(id)

@app.get("/ping")
async def ping():
    return {"message" : "Server is okay"}

@app.get("/movie/{id}")
async def get_movie(id : int) -> dict:
    movie = await get_movie_from_db(id)
    return {"id" : id, "movie" : movie}

@app.get("/sync-movie/{id}")
async def sync_get_movie(id : int) -> dict:
    movie = sync_get_movie_from_db(id)
    return {"id" : id, "movie" : movie}

@app.get("/movie_with_log/{id}")
async def get_movie_with_log(id : int, background_task : BackgroundTasks):
    movie = await get_movie_from_db(id)
    background_task.add_task(create_log, id)
    return {"id" : id, "movie" : movie}

async def create_log(id : int):
    await asyncio.sleep(2)
    print(f"A search was made for a movie with such an ID: {id}")
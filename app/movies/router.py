from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Path, Query
from fastapi.params import Depends

from app.movies.schemas import MovieCreate, MovieUpdate, MovieRead, MovieReplace
from app.movies.services import get_movie_from_db, sync_get_movie_from_db, create_log, set_movie_to_db, delete_movie_from_db, update_movie_from_db, update_part_movie_from_db, get_movies_from_db

router = APIRouter(prefix='/movies', tags=['Movies'])

@router.get("/{id}", response_model=MovieRead)
async def get_movie(id : Annotated[int, Path(title= "The id of film", gt=0)]) -> dict:
    dict_movie = await get_movie_from_db(id)
    return {"id" : id, **dict_movie}
    # return {"id" : id, "movie" : dict_movie.get("movie"), "year" : dict_movie.get("year")}.
    # !!! Оказывается, можно "распаковывать" словарь с помощью **dict

@router.post("/", response_model=MovieRead)
async def set_movie(model : MovieCreate) -> dict:
    id, dict_movie = await set_movie_to_db(model)
    return {"id": id, **dict_movie}

@router.put("/{id}", response_model=MovieRead)
async def update_movie(id : Annotated[int, Path(title= "The id of film",gt=0)], model : MovieReplace) -> dict:
    dict_movie = await update_movie_from_db(id, model)
    return {"id": id, **dict_movie}

@router.patch("/{id}", response_model=MovieRead)
async def update_part_movie(id : Annotated[int, Path(title= "The id of film",gt=0)], model : MovieUpdate) -> dict:
    dict_movie = await update_part_movie_from_db(id, model)
    return {"id": id, **dict_movie}

@router.delete("/{id}", response_model=MovieRead)
async def delete_movie(id : Annotated[int, Path(title= "The id of film",gt=0)]) -> dict:
    dict_movie = await delete_movie_from_db(id)
    return {"id": id, **dict_movie}

@router.get("/", response_model=list[MovieRead])
async def get_movies(limit : Annotated[int, Query(title="The number of returned movies", gt=0)]) -> list:
    list_movies = await get_movies_from_db(limit)
    return list_movies


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# DAY 1. Just for experiments
#
# | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@router.get("/sync/{id}")
async def sync_get_movie(id : int) -> dict:
    movie = sync_get_movie_from_db(id)
    return {"id" : id, "movie" : movie}

@router.get("/with_log/{id}")
async def get_movie_with_log(id : int, background_task : BackgroundTasks):
    movie = await get_movie_from_db(id)
    background_task.add_task(create_log, id)
    return {"id" : id, "movie" : movie}
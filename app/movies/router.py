from fastapi import APIRouter, BackgroundTasks
from app.movies.services import get_movie_from_db, sync_get_movie_from_db, create_log

router = APIRouter(prefix='/movies', tags=['Movies'])

@router.get("/{id}")
async def get_movie(id : int) -> dict:
    movie = await get_movie_from_db(id)
    return {"id" : id, "movie" : movie}


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
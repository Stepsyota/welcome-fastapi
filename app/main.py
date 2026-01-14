from fastapi import FastAPI
from app.movies.router import router as movie_router

app = FastAPI()
app.include_router(movie_router)

@app.get("/ping")
async def ping():
    return {"message" : "Server is okay"}
from pydantic import BaseModel


class MovieCreate(BaseModel):
    movie : str
    year : int

class MovieUpdate(BaseModel):
    movie : str | None = None
    year : int | None = None

class MovieReplace(BaseModel):
    movie: str
    year: int

class MovieRead(BaseModel):
    id : int
    movie : str
    year : int
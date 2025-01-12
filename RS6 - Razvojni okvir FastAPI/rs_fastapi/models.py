from pydantic import BaseModel

# pydantic klase su read-only

class FilmResponse(BaseModel):
  id: int
  naziv: str
  genre: str
  godina: int

from typing import Optional, Literal

class Kolegij(BaseModel):
  id: int
  naziv: str
  semestar: Literal[1, 2, 3, 4, 5, 6]
  ECTS: Optional[int] = 6
  opis: str
  profesor: str
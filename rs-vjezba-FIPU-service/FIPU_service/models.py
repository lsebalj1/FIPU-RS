from pydantic import BaseModel
from typing import Literal

class Kolegij(BaseModel):
    sifra : int
    naziv : str
    nositelj : str
    semestar : int
    godina_odrzavanja : int

class Student(BaseModel):
    jmbag : int 
    ime : str
    prezime : str
    kolegiji : list[int] = []
    godina_studija : int
    status: Literal["redovan", "izvanredan"]



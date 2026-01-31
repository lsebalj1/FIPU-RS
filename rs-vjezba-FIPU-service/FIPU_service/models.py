from pydantic import BaseModel, Field
from typing import Literal
import random

def create_jmbag():
    prvi_znakovi = "03030"
    
    for _ in range(5):
        random_dio = ''.join(str[random.randint(0, 9)])
    
    jmbag = prvi_znakovi + random_dio
    
    return jmbag

def create_sifra(naziv: str):
    kraj = "_FIPU"
    
    rijeci = naziv.split()
    
    if rijeci == 1:
        sifra = rijeci[0][:4].upper()
    else:
        sifra = ''.join([rijec[0].upper() for rijec in rijeci])
    
    return sifra + kraj

class Kolegij(BaseModel):
    sifra : str
    naziv : str
    nositelj : str
    semestar : int = Field(ge = 1, le = 8)
    godina_odrzavanja : int = Field(ge = 1, le = 5)

class Student(BaseModel):
    jmbag : str = Field(min_length=10, max_length=10)
    ime : str
    prezime : str
    kolegiji : list[int] = []
    godina_studija : int = Field(ge = 1, le = 5)
    status: Literal["redovan", "izvanredan"]

class StudentInput(BaseModel):
    ime : str
    prezime : str
    kolegiji : list[int] = []
    godina_studija : int = Field(ge = 1, le = 5)
    status: Literal["redovan", "izvanredan"]
    
class KolegijInput(BaseModel):
    naziv : str
    nositelj : str
    semestar : int = Field(ge = 1, le = 8)
    godina_odrzavanja : int = Field(ge = 1, le = 5)

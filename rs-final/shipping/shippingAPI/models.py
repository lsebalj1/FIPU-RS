from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

class Posiljka(BaseModel):
    id: int
    tezina: float = Field(gt= 0)
    status: Literal['u_pripremi', 'poslano', 'dostavljeno']
    datum_narudzbe: datetime
    email: str

class PosiljkaRequest(BaseModel):
    tezina: float
    email: str
    
# 5. zadatak (nadogradnja)

from typing_extensions import TypedDict

class Korisnik(TypedDict):
    ime: str
    prezime: str
    broj_telefona: str

class Adresa(TypedDict):
    grad: str
    ulica: str
    postanski_broj: str

class PosiljkaNew(BaseModel):
    id: int
    tezina: float
    status: Literal['u_pripremi', 'poslano', 'dostavljeno']
    datum_narudzbe: datetime
    email: str
    korisnik: Korisnik
    adresa: Adresa
    
    
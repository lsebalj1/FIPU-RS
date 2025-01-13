from pydantic import BaseModel

from datetime import datetime

from pydantic import BaseModel, Field

class KnjigaRequest(BaseModel):
  naslov: str
  autor: str
  broj_stranica: int = Field(ge=1) # broj stranica mora biti veći od 0
  godina_izdavanja: int = Field(ge=0, le=2024) # godina izdavanja mora biti između 0 i 2024

class KnjigaResponse(KnjigaRequest):
  id: int
  
class BaseProizvod(BaseModel):
  naziv: str
  cijena: float
  kategorija: str
  boja: str

class RequestProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
  pass # ne dodajemo niti jedan novi atribut

class ResponseProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
  id: int
  cijena_pdv: float
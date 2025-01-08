from pydantic import BaseModel


class CreateProizvod(BaseModel):
  naziv: str
  boja: str
  cijena: float

class Proizvod(BaseModel):
  id: int
  naziv: str
  boja: str
  cijena: float
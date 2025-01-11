from pydantic import BaseModel

# pydantic klase su read-only

class CreateProizvod(BaseModel):
  naziv: str
  boja: str
  cijena: float
  
class Proizvod(CreateProizvod):
  id: int
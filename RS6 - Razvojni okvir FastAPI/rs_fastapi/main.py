from fastapi import FastAPI
from models import CreateProizvod, ResponseProizvod

app = FastAPI()

@app.patch("/skladiste/{id_skladiste}")
def update_skladiste(proizvod: dict, id_skladiste: int, kategorija: str = "gradevinski_materijal",):
  pass
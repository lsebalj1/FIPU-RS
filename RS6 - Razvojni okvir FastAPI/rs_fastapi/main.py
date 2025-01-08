from fastapi import FastAPI
from models import CreateProizvod, ResponseProizvod

app = FastAPI()

proizvodi = [
  {"id" : 1, "naziv" : "Miš", "cijena": 50},
  {"id" : 2, "naziv" : "Tipkovnica", "cijena": 100},
  {"id" : 3, "naziv" : "Laptop", "cijena": 1000}
]
# route parametar - definiramo i u dekoratoru i u funkciji
# query parametar ? - ne definiramo u dekoratoru, ali da u funkciji i koristimo primitiv
# body - ne definiramo u dekoratoru, ali definiramo u funkciji kao dict ili Pydantic model


@app.get("/proizvodi/{proizvod_id}") # route
def dohvati_proizvode(proizvod_id: int, min_cijena : float): # hintati da bude int
  trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["id"] == proizvod_id and proizvod["cijena"] >= min_cijena), None)
  
  return {"trazeni_proizvod": trazeni_proizvod}

# HTTP body

@app.post("/proizvodi", response_model=list[ResponseProizvod])
def dodaj_proizvod(proizvod : CreateProizvod): # http body
  print("proizvod: ", proizvod)
  
  new_id = len(proizvodi) + 1

  proizvod_sa_id = ResponseProizvod(id=new_id, **proizvod.model_dump())
  #proizvodi.append(proizvod)
  
  return {"proizvod": proizvod_sa_id}
from fastapi import FastAPI
from models import KorisnikCreate, KorisnikResponse
from datetime import datetime
import random
app = FastAPI()

korisnici = []

@app.post("/korisnici", response_model=KorisnikResponse)
def registracija_korisnika(korisnik: KorisnikCreate):

  lozinka_hash = str(hash(korisnik.lozinka_text)) # simuliramo heširanje lozinke
  datum_registracije = datetime.now() # trenutni datum i vrijeme registracije
  korisnik_spreman_za_pohranu = KorisnikResponse(**korisnik.model_dump(), lozinka_hash=lozinka_hash, datum_registracije=datum_registracije)

  print(f"Korisnik spreman za pohranu: {korisnik_spreman_za_pohranu}")

  korisnici.append(korisnik_spreman_za_pohranu.model_dump())
  return korisnik_spreman_za_pohranu
from fastapi import APIRouter, HTTPException
from models import Posiljka, PosiljkaRequest
from datetime import datetime

router = APIRouter(prefix="/posiljke")


posiljke = []
id_counter = 1

@router.get("/", response_model=list[Posiljka])
async def list_posiljke():
    return posiljke

# ispravno, ali je zakomentirano zbog nadogradnje rute (5. zadatak)
"""
@router.post("/", response_model=Posiljka)
async def create_posiljka(request: PosiljkaRequest):
    global id_counter
    posiljka = Posiljka(
        id=id_counter,
        tezina=request.tezina,
        status='u_pripremi',
        email=request.email,
        datum_narudzbe=datetime.now(),
    )
    posiljke.append(posiljka)
    id_counter += 1
    return posiljka

@router.get("/", response_model=list[Posiljka])
async def list_posiljke():
    return posiljke
"""

# 5. zadatak (nadogradnja servisa)

import aiohttp
from models import PosiljkaNew

async def get_user_from_usersAPI(email: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://usersapi:8080/korisnici/{email}') as response:
            if response.status != 200:
                return None
            return await response.json()

@router.post("/", response_model=PosiljkaNew)
async def create_posiljka(request: PosiljkaRequest):
    global id_counter

    korisnik_podaci = await get_user_from_usersAPI(request.email)
    if not korisnik_podaci:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen")

    
    korisnik = {
        "ime": korisnik_podaci["ime"],
        "prezime": korisnik_podaci["prezime"],
        "broj_telefona": korisnik_podaci["broj_telefona"]
    }
    adresa = korisnik_podaci["adresa"] 

    posiljka = PosiljkaNew(
        id=id_counter,
        tezina=request.tezina,
        status="u_pripremi",
        email=request.email,
        datum_narudzbe=datetime.now(),
        korisnik=korisnik,
        adresa=adresa
    )
    posiljke.append(posiljka)
    id_counter += 1
    return posiljka
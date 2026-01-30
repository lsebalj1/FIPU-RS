from fastapi import APIRouter
from models import Posiljka, PosiljkaRequest, StatusPosiljke
from datetime import datetime

router = APIRouter()

posiljke = []

posiljka_id_counter = 1

@router.get("/posiljke", response_model=list[Posiljka])
def get_posiljke():
    return posiljke

@router.post("/posiljke", response_model=Posiljka)
def create_posiljka(posiljka_request: PosiljkaRequest):
    global posiljka_id_counter
    
    nova_posiljka = Posiljka(
        id=posiljka_id_counter,
        tezina=posiljka_request.tezina,
        status=StatusPosiljke.u_pripremi,
        email=posiljka_request.email,
        datum_narudzbe=datetime.now()
    )
    
    posiljke.append(nova_posiljka)
    
    posiljka_id_counter += 1
    
    return nova_posiljka
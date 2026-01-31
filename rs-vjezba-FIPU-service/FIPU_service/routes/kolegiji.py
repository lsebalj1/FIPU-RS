from fastapi import APIRouter, HTTPException, status
from models import Kolegij, KolegijInput, create_sifra

kolegiji = [
    {
        "sifra": "PROG_FIPU", 
        "naziv": "Programiranje", 
        "nositelj": "Tihomir Orehovački", 
        "semestar": 1, 
        "godina_odrzavanja": 1
    },
    {
        "sifra": "WA_FIPU", 
        "naziv": "Web aplikacije", 
        "nositelj": "Nikola Tanković", 
        "semestar": 5, 
        "godina_odrzavanja": 3
    },
    {
        "sifra": "RS_FIPU", 
        "naziv": "Raspodijeljeni sustavi", 
        "nositelj": "Nikola Tanković", 
        "semestar": 1, 
        "godina_odrzavanja": 4
    },
    {
        "sifra": "UPP_FIPU", 
        "naziv": "Upravljanje poslovnim procesima", 
        "nositelj": "Darko Etinger", 
        "semestar": 5, 
        "godina_odrzavanja": 3
    }
]

router = APIRouter()

@router.get("/kolegiji", response_model = list[Kolegij])
def get_kolegiji():
    return kolegiji

@router.get("/kolegiji/{sifra}", response_model = Kolegij)
def get_kolegij_sifra(sifra: str):
    for kolegij in kolegiji:
        if kolegij["sifra"] == sifra:
            return kolegij
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opis greške")
    
@router.post("/kolegiji", response_model = Kolegij)
def new_kolegij(kolegij_input : KolegijInput):
    nova_sifra = create_sifra(kolegij_input.naziv)
    
    novi_kolegij = Kolegij(
        sifra = nova_sifra,
        naziv = kolegij_input.naziv,
        nositelj = kolegij_input.nositelj,
        semestar = kolegij_input.semestar,
        godina_odrzavanja = kolegij_input.godina_odrzavanja
    )
    
    kolegiji.append(novi_kolegij)
    

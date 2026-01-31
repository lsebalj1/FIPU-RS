from fastapi import APIRouter, HTTPException
from models import Student

studenti = [
{"JMBAG": "0303097567", "ime": "Marko", "prezime": "Marković", "kolegiji":
[], "godina_studija": 1, "status": "redovan"},
{"JMBAG": "0303011920", "ime": "Iva", "prezime": "Ivić", "kolegiji": [],
"godina_studija": 4, "status": "izvanredan"},
{"JMBAG": "0303088112", "ime": "Ana", "prezime": "Anić", "kolegiji": [],
"godina_studija": 1, "status": "redovan"}
]

router = APIRouter()

@router.get("/studenti", response_model = list[Student])
def get_studenti():
    return studenti

@router.get("/studenti/{jmbag}", response_model = list[Student])
def get_student_jmbag(jmbag: str):
    for student in studenti:
        if student["JMBAG"] == jmbag:
            return student
        
    raise HTTPException(status_code=404, detail = "Student nije pronaden")


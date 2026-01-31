from fastapi import APIRouter, HTTPException, status
from models import Student, StudentInput, create_jmbag

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

@router.get("/studenti/{jmbag}", response_model = Student)
def get_student_jmbag(jmbag: str):
    for student in studenti:
        if student["JMBAG"] == jmbag:
            return student
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opis greške")

@router.post("/studenti", response_model = Student)
def new_student(student_input : StudentInput):
    novi_jmbag = create_jmbag()
    
    novi_student = Student(
        jmbag = novi_jmbag,
        ime = student_input.ime,
        prezime = student_input.prezime,
        kolegiji = student_input.kolegiji,
        godina_studija = student_input.godina_studija,
        status = student_input.status
    )
    
    studenti.append(novi_student)


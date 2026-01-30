from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class StatusPosiljke(str, Enum):
    u_pripremi = "u_pripremi"
    poslano = "poslano"
    dostavljeno = "dostavljeno"

class PosiljkaRequest(BaseModel):
    tezina: float
    email: EmailStr

class Posiljka(BaseModel):
    id: int
    tezina: float
    status: StatusPosiljke
    email: EmailStr
    datum_narudzbe: datetime
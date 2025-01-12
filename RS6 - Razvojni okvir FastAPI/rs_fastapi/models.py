from pydantic import BaseModel

from datetime import datetime

class KorisnikBase(BaseModel):
  ime: str
  prezime: str
  email: str

class KorisnikCreate(KorisnikBase):
  lozinka_text: str

class KorisnikResponse(KorisnikBase):
  lozinka_hash: str
  datum_registracije: datetime # hintamo složeni objekt tipa datetime
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

from pydantic import BaseModel

class Admin(BaseModel):
  korisnicko_ime: str
  token: str

administratori = [
  {"korisnicko_ime": "secret_admin_007", "token": "super_secret_admin_token007"},
  {"korisnicko_ime": "secret_admin_123", "token": "admin_token123"},
  {"korisnicko_ime": "secret_admin_456", "token": "admin_token456"}
]

def provjeri_token(token: str):
  for admin in administratori:
    if admin["token"] == token:
      return Admin(**admin) # vraćamo instancu Admin klase
  raise HTTPException(status_code=401, detail="Nemate ovlasti za pristup ovim podacima")

@app.get("/tajni_podaci")
def get_tajni_podaci(admin: Admin = Depends(provjeri_token)): # koristimo Depends funkciju za "ubrizgavanje ovisnosti"
  return {"tajni_podaci": "šifra za sef je 1234"}

@app.put("/tajni_podaci")
def update_tajni_podaci(podaci: dict, admin: Admin = Depends(provjeri_token)):
  # ažuriramo podatke...
  print(f"Podatke ažurirao admin {admin.korisnicko_ime}")
  return {"poruka": "Podaci uspješno ažurirani"}

@app.delete("/tajni_podaci")
def delete_tajni_podaci(admin: Admin = Depends(provjeri_token)):
  # brišemo podatke...
  print(f"Podatke izbrisao admin {admin.korisnicko_ime}")
  return {"poruka": "Podaci uspješno obrisani"}

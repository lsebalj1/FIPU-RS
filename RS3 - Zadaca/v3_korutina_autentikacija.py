#korutina autentikacija
# Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
#od ključeva korisnicko_ime , email i lozinka
# Unutar korutine simulirajte provjeru korisničkog
#imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
# provjera traje 3 sekunde

import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autentifikacija(korisnik: dict):

async def autorizacija(korisnik: dict, lozinka: str):


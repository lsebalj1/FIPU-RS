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

async def autentifikacija(korisnik: dict) -> dict: 
    await asyncio.sleep(3)

    for korisnik_u_bazi in baza_korisnika:
        if (korisnik_u_bazi['korisnicko_ime'] == korisnik['korisnicko_ime'] and 
            korisnik_u_bazi['email'] == korisnik['email']):
            
            rezultat = {
                'korisnicko_ime': korisnik['korisnicko_ime'],
                'email': korisnik['email'],
                'autentifikacija': True
            }
            return rezultat  

    rezultat = {
        'korisnicko_ime': korisnik['korisnicko_ime'],
        'email': korisnik['email'],
        'autentifikacija': False
    }

    print("Korisnik {korisnik} nije pronađen.")
    
    return rezultat

async def autorizacija(korisnik: dict, lozinka: str) -> dict:
    await asyncio.sleep(2)
    
    for korisnik_u_bazi in baza_lozinka:
        if (korisnik_u_bazi['korisnicko_ime'] == korisnik['korisnicko_ime'] and 
            korisnik_u_bazi['lozinka'] == lozinka):
            
            rezultat = {
                'korisnicko_ime': korisnik['korisnicko_ime'],
                'autorizacija': True
            }

            print(f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna.")
            return rezultat
    
    rezultat = {
        'korisnicko_ime': korisnik['korisnicko_ime'],
        'autorizacija': False
    }
    
    print(f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna.")
    return rezultat

async def main():
    korisnici = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'nepostojeci', 'email': 'fake@gmail.com', 'lozinka': 'fake123'}
    ]
    
    autentifikacija_zadaci = [asyncio.create_task(autentifikacija(k)) for k in korisnici]
    autentifikacija_rezultati = await asyncio.gather(*autentifikacija_zadaci)
    
    autorizacija_zadaci = []
    for i, rez in enumerate(autentifikacija_rezultati):
        if rez['autentifikacija']:
            autorizacija_zadaci.append(
                asyncio.create_task(autorizacija(rez, korisnici[i]['lozinka']))
            )
    
    if autorizacija_zadaci:
        autorizacija_rezultati = await asyncio.gather(*autorizacija_zadaci)

        for rez in autorizacija_rezultati:
            status = "✓" if rez['autorizacija'] else "✗"
            print(f"{status} {rez['korisnicko_ime']}: {rez['autorizacija']}")
    else:
        print("Nema korisnika za autorizaciju.")

asyncio.run(main())

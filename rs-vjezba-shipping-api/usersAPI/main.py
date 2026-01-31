from aiohttp import web
import asyncio

korisnici = [
    {"id": 1, "ime": "Ana", "prezime": "Anić", "email": "aanic@gmail.com",
     "broj_telefona": "0911234453", "adresa": {"grad": "Zagreb", "ulica": "Ilica 15",
     "postanski_broj": "10000"}},
    {"id": 2, "ime": "Marko", "prezime": "Markić", "email": "mmarkic@gmail.com",
     "broj_telefona": "0919876543", "adresa": {"grad": "Split", "ulica": "Riva 3",
     "postanski_broj": "21000"}},
    {"id": 3, "ime": "Ivana", "prezime": "Ivić", "email": "iivic@gmail.com",
     "broj_telefona": "0921234567", "adresa": {"grad": "Rijeka", "ulica": "Korzo 5",
     "postanski_broj": "51000"}},
    {"id": 4, "ime": "Petar", "prezime": "Perić", "email": "pperic@gmail.com",
     "broj_telefona": "0952345678", "adresa": {"grad": "Osijek", "ulica": "Europska avenija 10",
     "postanski_broj": "31000"}},
    {"id": 5, "ime": "Maja", "prezime": "Majić", "email": "mmajic@gmail.com",
     "broj_telefona": "0973456789", "adresa": {"grad": "Zadar", "ulica": "Kalelarga 20",
     "postanski_broj": "23000"}},
    {"id": 6, "ime": "Luka", "prezime": "Lukić", "email": "llukic@gmail.com",
     "broj_telefona": "0998765432", "adresa": {"grad": "Dubrovnik", "ulica": "Stradun 8",
     "postanski_broj": "20000"}}
]

async def get_korisnici(request):
    return web.json_response(korisnici)

async def get_korisnik_by_email(request):
    email = request.match_info.get('email')
    
    if '@' not in email or '.' not in email:
        return web.json_response(
            {"error": "Neispravan format email adrese. Email mora sadržavati '@' i '.'"},
            status=400
        )
    
    korisnik = next((k for k in korisnici if k['email'] == email), None)
    
    if korisnik is None:
        return web.json_response(
            {"error": f"Korisnik s email adresom '{email}' nije pronađen"},
            status=404
        )
    
    return web.json_response(korisnik)


async def main():
    app = web.Application()
    app.router.add_get('/korisnici', get_korisnici)
    app.router.add_get('/korisnici/{email}', get_korisnik_by_email)
    
    print("Poslužitelj pokrenut na http://localhost:8001")
    print("Dostupne rute:")
    print("  GET  http://localhost:8001/")
    print("  GET  http://localhost:8001/korisnici")
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8001)
    await site.start()
    
    print("Poslužitelj pokrenut!")
    await asyncio.Event().wait()

asyncio.run(main())
from aiohttp import web
import asyncio
import hashlib

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash":
        "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},  
    {"korisnicko_ime": "markoMaric", "lozinka_hash":
        "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},  
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash":
        "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},  
    {"korisnicko_ime": "Nada000", "lozinka_hash":
        "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}   
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def register(request):
    try:
        data = await request.json()
    except:
        return web.json_response({"error": "Neispravan format podataka (očekuje se JSON)"}, status=400)

    username = data.get("korisnicko_ime")
    password = data.get("lozinka")

    if not username or not password:
        return web.json_response({"error": "Nedostaju polja 'korisnicko_ime' ili 'lozinka'"}, status=400)

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == username:
            return web.json_response({"error": "Korisničko ime je zauzeto"}, status=409) 

    novi_hash = hash_data(password)
    
    novi_korisnik = {
        "korisnicko_ime": username,
        "lozinka_hash": novi_hash
    }
    
    korisnici.append(novi_korisnik)

    return web.json_response({
        "message": f"Korisnik '{username}' uspješno registriran.",
        "korisnik": {
            "korisnicko_ime": username,
            "lozinka_hash": novi_hash 
        }
    }, status=201)

async def main():
    app = web.Application()
    print("Posluzitelj pokrenut!")
    app.router.add_post('/register', register)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Poslužitelj pokrenut!")
    await asyncio.Event().wait()

asyncio.run(main())
from aiohttp import web
import aiohttp
import asyncio

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info['id'])
    
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod is None:
        return web.json_response(
            {'error': 'Proizvod s traženim ID-em ne postoji'}, 
            status=404
        )
    
    return web.json_response(proizvod)

async def post_narudzba(request):
    data = await request.json()
    proizvod_id = data.get('proizvod_id')
    kolicina = data.get('kolicina')

    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod is None:
        return web.json_response(
            {'error': 'Proizvod s traženim ID-em ne postoji'}, 
            status=404
        )

    narudzba = {
        'proizvod_id': proizvod_id,
        'kolicina': kolicina
    }
    narudzbe.append(narudzba)
    
    return web.json_response(narudzbe, status=201)

async def start_server():
    app = web.Application()
    app.router.add_get('/proizvodi', get_proizvodi)
    app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)
    app.router.add_post('/narudzbe', post_narudzba)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    
    print("Poslužitelj pokrenut na http://localhost:8081")
    return runner

async def test_client():
    async with aiohttp.ClientSession() as session:
        print("\nTEST 1: Dohvati sve proizvode")
        async with session.get('http://localhost:8081/proizvodi') as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 2: Dohvati proizvod s ID-em 1")
        async with session.get('http://localhost:8081/proizvodi/1') as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 3: Dohvati proizvod s ID-em 3")
        async with session.get('http://localhost:8081/proizvodi/3') as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 4: Dohvati nepostojeći proizvod (ID 999)")
        async with session.get('http://localhost:8081/proizvodi/999') as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 5: Kreiraj narudžbu za proizvod ID 1, količina 2")
        narudzba_data = {'proizvod_id': 1, 'kolicina': 2}
        async with session.post('http://localhost:8081/narudzbe', json=narudzba_data) as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 6: Kreiraj narudžbu za proizvod ID 5, količina 1")
        narudzba_data = {'proizvod_id': 5, 'kolicina': 1}
        async with session.post('http://localhost:8081/narudzbe', json=narudzba_data) as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")
        
        print("TEST 7: Kreiraj narudžbu za nepostojeći proizvod (ID 999)")
        narudzba_data = {'proizvod_id': 999, 'kolicina': 3}
        async with session.post('http://localhost:8081/narudzbe', json=narudzba_data) as response:
            print(f"Status: {response.status}")
            print(f"Odgovor: {await response.json()}\n")

async def main():
    runner = await start_server()
    await asyncio.sleep(1)
    await test_client()
    
    print("Testiranje završeno. Poslužitelj nastavlja raditi...")
    await asyncio.Event().wait()

asyncio.run(main())
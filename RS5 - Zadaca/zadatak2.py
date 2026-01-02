from aiohttp import web
import asyncio

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "količina": 10},
    {"naziv": "Miš", "cijena": 100, "količina": 50},
    {"naziv": "Tipkovnica", "cijena": 200, "količina": 30}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    novi_proizvod = await request.json()
    print(f"Primljeni podaci: {novi_proizvod}")
    proizvodi.append(novi_proizvod)
    return web.json_response(proizvodi)

async def main():
    app = web.Application()
    app.router.add_get('/proizvodi', get_proizvodi)
    app.router.add_post('/proizvodi', post_proizvodi)
    
    print("Poslužitelj pokrenut na http://localhost:8081")
    print("Dostupne rute:")
    print("  GET  http://localhost:8081/proizvodi")
    print("  POST http://localhost:8081/proizvodi")
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    
    print("Poslužitelj pokrenut!")
    await asyncio.Event().wait()

asyncio.run(main())
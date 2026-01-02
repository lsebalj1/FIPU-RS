from aiohttp import web
import asyncio

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def get_punoljetni(request):
    punoljetni = list(filter(lambda k: k["godine"] > 18, korisnici))
    return web.json_response(punoljetni)

async def main():
    app = web.Application()
    app.router.add_get('/punoljetni', get_punoljetni)
    
    print("Poslužitelj pokrenut na http://localhost:8082")
    print("Dostupne rute:")
    print("  GET  http://localhost:8082/punoljetni")
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8082)
    await site.start()
    
    print("Poslužitelj pokrenut!")
    await asyncio.Event().wait()

asyncio.run(main())
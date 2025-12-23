from aiohttp import web

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

app = web.Application()
app.router.add_get('/punoljetni', get_punoljetni)

if __name__ == '__main__':
    print("Pokrećem poslužitelj na http://localhost:8082")
    print("Dostupne rute:")
    print("  GET  http://localhost:8082/punoljetni")
    web.run_app(app, port=8082)
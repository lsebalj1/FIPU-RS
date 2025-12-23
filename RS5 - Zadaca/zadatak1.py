from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "količina": 10},
    {"naziv": "Miš", "cijena": 100, "količina": 50},
    {"naziv": "Tipkovnica", "cijena": 200, "količina": 30}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)

if __name__ == '__main__':
    web.run_app(app, port=8081)
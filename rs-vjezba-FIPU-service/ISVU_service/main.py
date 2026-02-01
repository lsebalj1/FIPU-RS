from aiohttp import web
import asyncio
'''
docker build -t isvu-service .
docker run -p 9000:9000 isvu-service  
'''
ispitni_rokovi = [
{"sifra": "PROG_FIPU", "ispitni_rok": "Ispitni rok 1", "datum": "2025-02-15"},
{"sifra": "PROG_FIPU", "ispitni_rok": "Ispitni rok 2", "datum": "2025-06-15"},
{"sifra": "PROG_FIPU", "ispitni_rok": "Ispitni rok 3", "datum": "2025-09-15"},
{"sifra": "WA_FIPU", "ispitni_rok": "Ispitni rok 1", "datum": "2025-02-20"},
{"sifra": "WA_FIPU", "ispitni_rok": "Ispitni rok 2", "datum": "2025-06-20"},
{"sifra": "RS_FIPU", "ispitni_rok": "Ispitni rok 1", "datum": "2025-02-25"},
{"sifra": "RS_FIPU", "ispitni_rok": "Ispitni rok 2", "datum": "2025-06-25"},
{"sifra": "UPP_FIPU", "ispitni_rok": "Ispitni rok 1", "datum": "2025-03-01"},
{"sifra": "UPP_FIPU", "ispitni_rok": "Ispitni rok 2", "datum": "2025-07-01"},]

app = web.Application()

async def get_ispitni_rok(session):
    sifra = session.match_info['sifra']

    for rok in ispitni_rokovi:
        if rok["sifra"] == sifra:
            return web.json_response(rok, status= 200)
    
    return web.json_response(
        {"error" : "{sifra} ne postoji"},
        status = 404
    )

app.router.add_get("/ispitni_rokovi/{sifra}", get_ispitni_rok)

async def start_server(): 
    runner = web.AppRunner(app) 
    await runner.setup() 
    host = '0.0.0.0'
    port = 9000
    site = web.TCPSite(runner, host, port) 
    await site.start() 

async def main():
    asyncio.create_task(start_server())
    


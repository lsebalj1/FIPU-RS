from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

app = web.Application()

korisnici = [
  {"id": 1, "ime": "Ivo", "godine": 25},
  {"id": 2, "ime": "Ana", "godine": 22},
  {"id": 3, "ime": "Marko", "godine": 19},
  {"id": 4, "ime": "Maja", "godine": 21},
  {"id": 5, "ime": "Iva", "godine": 40}
]

async def get_users(request):
  return web.json_response(korisnici, status=200)

async def get_user(request):
  ime = request.match_info["ime"]
  
  for korisnik in korisnici:
    if korisnik["ime"] == ime:
      return web.json_response(korisnik, status = 200)

  return web.json_response({"message": f"Greška! Ne pronalazim korisnika {ime}"}, status=404)
  

app.router.add_get('/korisnici', get_users)
app.router.add_get('/korisnici/{ime}', get_user)

async def pokreni_posluzitelj():
  runner = AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8080)
  await site.start()
  print("Pokrećem poslužitelj...")

async def main():
  
  await pokreni_posluzitelj()
  
  async with aiohttp.ClientSession() as session:
    print("Klijentska sesija otvorena")
    
    # GET /korisnici
    odgovor = await session.get("http://localhost:8080/korisnici")
    odgovor_list = await odgovor.json()
    print("Odgovor /korisnici", odgovor_list)
    
    # GET /korisnici/{ime} URL parametar
    
    odgovor_2 = await session.get("http://localhost:8080/korisnici/1")
    odgovor_2_list = await odgovor_2.json()
    
    print("Odgovor /korisnici/Perica", odgovor_2_list)
    
asyncio.run(main()) # pokreće klijentsku sesiju

web.run_app
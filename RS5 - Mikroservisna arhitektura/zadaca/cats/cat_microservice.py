from aiohttp import web
import asyncio, aiohttp
app = web.Application()

async def get_fact(session):
  print("Šaljem zahtjev...")
  response = await session.get("https://catfact.ninja/fact")
  response_dict = await response.json()
  return response_dict

async def fetch_cats(request):
  amount = int(request.match_info.get("amount"))
  
  async with aiohttp.ClientSession() as session:
    list_of_facts = await asyncio.gather(*[get_fact(session) for _ in range(amount)])
  print(list_of_facts)
  return web.json_response(list_of_facts, status=200)

app.router.add_get("/cats/{amount}", fetch_cats) 

web.run_app(app, port=8086)
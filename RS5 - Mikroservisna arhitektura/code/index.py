import asyncio
import aiohttp
from aiohttp import web  #Server API - za poslužitelje

app = web.Application()


def handler_function(request): # request = HTTP request
  data = {'ime': 'Ivo', 'prezime': 'Ivić', 'godine': 25}
  return web.json_response(data) # JSON response

async def post_handler(request):
  data = await request.json() # Deserijalizacija JSON podataka
  print(data) # Ispis podataka u terminal
  return web.json_response(data)

app.router.add_get("/", handler_function)
app.router.add_post("/", post_handler)

web.run_app(app, host="localhost", port=8080) # pokretanje poslužitelja


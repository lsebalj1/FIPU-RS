import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

async def handle_service2(request):
  await asyncio.sleep(2)
  return web.json_response({"message" : "Pozdrav iz mikroservisa 2"})

app.router.add_get('/', handle_service2)

if __name__ == "__main__":
  web.run_app(app, port=8082)

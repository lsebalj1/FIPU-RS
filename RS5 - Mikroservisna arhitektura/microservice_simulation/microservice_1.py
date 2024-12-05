import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

async def handle_service1(request):
  await asyncio.sleep(1)
  return web.json_response({"message" : "Pozdrav iz mikroservisa 1"})

app.router.add_get('/', handle_service1)

# python3 microservice_1.py
if __name__ == "__main__":
  web.run_app(app, port=8081)

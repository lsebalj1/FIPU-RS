# microservice_2.py
from aiohttp import web
from asyncio import sleep

async def handle_service2(request):
  await sleep(2)
  return web.json_response({"message": "Hello from Microservice 2"})

app = web.Application()
app.router.add_get('/', handle_service2)

if __name__ == "__main__":
    web.run_app(app, port=8082)
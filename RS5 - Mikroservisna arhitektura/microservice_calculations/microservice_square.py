# microservice_square.py
from aiohttp import web

async def handle_squares(request):
  data = await request.json()
  data_brojevi = data.get("podaci")
  kvadrati = [i ** 2 for i in data_brojevi]
  return web.json_response({"kvadrati": kvadrati})

app = web.Application()
app.router.add_post('/kvadrati', handle_squares)
web.run_app(app, host='localhost', port=8083)
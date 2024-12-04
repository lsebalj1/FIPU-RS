from aiohttp import web

async def handle_squares(request):
  data = await request.json()
  data_brojevi = data.get("podaci")
  korijeni = [i ** 0.5 for i in data_brojevi]
  return web.json_response({"korijeni": korijeni})

app = web.Application()
app.router.add_post('/korijeni', handle_squares)
web.run_app(app, host='localhost', port=8084)
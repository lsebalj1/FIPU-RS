from aiohttp import web
import asyncio, aiohttp

app = web.Application()

async def handle_facts(request):
  facts = await request.json() # REQUEST BODY
  
  filtered_facts = list(filter(lambda fact: "cat" in fact["fact"].lower(), facts))
  print("len filtered_facts", len(filtered_facts))
  return web.json_response(filtered_facts, status=200)

app.router.add_get("/facts", handle_facts) 

web.run_app(app, port=8088)
from aiohttp import web
# koji endpoint moramo definirati?
app = web.Application()

async def sum_handler(request):
  podaci = await request.json()
  brojevi = podaci.get("brojevi")
  
  print("brojevi:", brojevi)
  print("brojevi type:", type(brojevi))
  
  zbroj = sum(brojevi) # vracamo zbroj podataka
  
  return web.json_response({"zbroj" : zbroj})

app.router.add_post("/zbroj", sum_handler)

web.run_app(app, host='localhost', port=8081)

# INPUT: JSON s listom brojeva [1,2,3,4,5]
# OUTPUT: JSON s ključem zbroj : []
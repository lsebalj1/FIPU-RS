from aiohttp import web

app = web.Application()

async def ratio_handler(request):
  podaci = await request.json()
  brojevi = podaci.get("brojevi")
  zbroj = podaci.get("zbroj")

  ratio_list = [round(broj/zbroj, 2) for broj in brojevi]
  
  print("ratio_list", ratio_list)
  
  return web.json_response({"ratio_list" : ratio_list})

app.router.add_post("/ratio", ratio_handler)

web.run_app(app, host='localhost', port=8082)

# INPUT: JSON s listom brojeva [1,2,3,4,5]
# OUTPUT: JSON s ključem zbroj : []
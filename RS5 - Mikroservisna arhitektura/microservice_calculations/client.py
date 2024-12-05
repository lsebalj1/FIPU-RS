import aiohttp
import asyncio

async def fetch_service_1(brojevi):
  async with aiohttp.ClientSession() as session:
    podatak_koji_saljemo = {"brojevi" : brojevi}
    rezultat = await session.post("http://localhost:8081/zbroj",
                                  json=podatak_koji_saljemo)
    return await rezultat.json()
  
async def fetch_service_2(brojevi, zbroj):
  async with aiohttp.ClientSession() as session:
    podatak_koji_saljemo = {"brojevi" : brojevi, "zbroj": zbroj}
    rezultat = await session.post("http://localhost:8082/ratio",
                                  json=podatak_koji_saljemo)
    return await rezultat.json()  
  
async def main():
  print("Pokrećem main korutinu")
  brojevi = [i for i in range(1,11)]
  print(brojevi)
  
  zbroj_dict = await fetch_service_1(brojevi) # rezultat: {"zbroj": neki_zbroj}
  
  zbroj = zbroj_dict.get("zbroj")
  
  rezultat_drugog_mikroservisa = await fetch_service_2(brojevi, zbroj)
  
  print(rezultat_drugog_mikroservisa)

asyncio.run(main())
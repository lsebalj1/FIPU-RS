import aiohttp
import asyncio


async def fetch_square_data(session, data_json):
  response = await session.post('http://localhost:8083/kvadrati', json=data_json)
  return await response.json()

async def fetch_sqrt_data(session, data_json):
  response = await session.post('http://localhost:8084/korijeni', json=data_json)
  return await response.json()

async def main():
  print("Pokrećem main korutinu")
  data = [i for i in range(1, 11)]
  data_json = {"podaci": data}
  
  async with aiohttp.ClientSession() as session:
      # Konkurentno pozivanje mikroservisa
      microservice_square_data, microservice_sqrt_data = await asyncio.gather(fetch_square_data(session, data_json), fetch_sqrt_data(session, data_json))
      
      # Ekstrakcija podataka
      kvadrati = microservice_square_data.get("kvadrati")
      korijeni = microservice_sqrt_data.get("korijeni")
      
      print(f"Zbroj kvadrata: {sum(kvadrati)}")
      print(f"Zbroj korijena: {sum(korijeni)}")
      print(f"Ukupni zbroj: {sum(kvadrati) + sum(korijeni)}")

asyncio.run(main())

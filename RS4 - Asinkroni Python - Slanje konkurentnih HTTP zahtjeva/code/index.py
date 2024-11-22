import requests
import time
import aiohttp
import asyncio

async def get_cat_fact(session, i):
  print(f"Šaljem zahtjev {i} o mački...")
  response = await session.get("https://catfact.ninja/fact")
  response_json = await response.json()
  print(response_json)
  return response_json

async def main():
  start_time = time.time()
  async with aiohttp.ClientSession() as session:
    lista_taskova = [asyncio.create_task(get_cat_fact(session, i+1))  for i in range(15)]
    
    print(lista_taskova)
    
    rezultat = await asyncio.gather(*lista_taskova)
    
    print(rezultat)
    
    end_time = time.time()
    #print(rezultat)
  print(f"Vrijeme izvršavanja programa je {end_time - start_time:.2f} sec")

asyncio.run(main())
# client.py
import aiohttp
import asyncio
import time

async def fetch_service():
  async with aiohttp.ClientSession() as session:
    service_1 = session.get('http://localhost:8081/')
    service_2 = session.get('http://localhost:8082/')

    tasks = [asyncio.create_task(service_1), asyncio.create_task(service_2)]
    rezultati = await asyncio.gather(*tasks)

    return [await rezultat.json() for rezultat in rezultati] # radi!

async def main():
  print("Pokrećem main korutinu")
  start_time = time.time()
  results = await fetch_service()
  end_time = time.time()
  print(results)
  print(f"Vrijeme izvršavanja: {end_time - start_time:.2f} sekundi")

asyncio.run(main())
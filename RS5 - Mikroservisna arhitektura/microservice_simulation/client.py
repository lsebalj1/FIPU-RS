import asyncio
import aiohttp
import time

async def fetch_service1():
  async with aiohttp.ClientSession() as session:
    response = await session.get('http://localhost:8081/')
    return await response.json()

async def fetch_service2():
  async with aiohttp.ClientSession() as session:
    response = await session.get('http://localhost:8082/')
    return await response.json()

async def main():
  print("Pokrećem glavnu korutinu...")

  responses = await asyncio.gather(fetch_service1(), fetch_service2())

  print(responses)
    

asyncio.run(main())
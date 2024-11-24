
import aiohttp
import asyncio

async def get_cat_fact(session):
  response = await session.get("https://catfact.ninja/fact")
  fact_dict = await response.json()
  print(fact_dict['fact'])
  return fact_dict['fact']

async def main():
  async with aiohttp.ClientSession() as session:
    cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
    rezulat = await asyncio.gather(*cat_fact_korutine)
    
    [[{}, {},{}], [{},{},{}]]
    #rezultat["name"]
    
    # transformacija ovdje
    # lista1 = []
    # lista2 = []
    # lista3 = []
    # print print print
    
asyncio.run(main())
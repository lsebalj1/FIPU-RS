import aiohttp
import asyncio
from faker import Faker

faker = Faker()

async def posalji_posiljku(session, posiljka):
    async with session.post("http://127.0.0.1:8000/posiljke", json=posiljka) as resp:
        return await resp.json()

async def simuliraj_posiljke(n):
    posiljke = []
    for _ in range(n):
        posiljke.append({
            "tezina": faker.pyfloat(min_value=5, max_value=30, right_digits=2),
            "email": faker.email()
        })
    return posiljke

async def main():
    async with aiohttp.ClientSession() as session:
        posiljke = await simuliraj_posiljke(50)
        tasks = [posalji_posiljku(session, posiljka) for posiljka in posiljke]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

if __name__ == '__main__':
    asyncio.run(main())

import aiohttp
import asyncio
from faker import Faker

SHIPPING_API_URL = "http://127.0.0.1:8000"

faker = Faker()

def simuliraj_posiljke(n: int):
    posiljke = []
    for _ in range(n):
        posiljka = {
            "tezina": faker.pyfloat(min_value=5, max_value=30, right_digits=2),
            "email": faker.email()
        }
        posiljke.append(posiljka)
    return posiljke

async def posalji_posiljku(session, posiljka):
    async with session.post(f"{SHIPPING_API_URL}/posiljke", json=posiljka) as response:
        rezultat = await response.json()
        return rezultat

async def main():
    async with aiohttp.ClientSession() as session:
        posiljke = simuliraj_posiljke(50)

        posiljke_rezultati = await asyncio.gather(
            *[posalji_posiljku(session, posiljka) for posiljka in posiljke]
        )

        for rezultat in posiljke_rezultati:
            print(rezultat)

asyncio.run(main())
import asyncio

osjetljivi_podaci = [
    {
        "prezime": "Horvat",
        "broj_kartice": "1234567812345678",
        "CVV": "123"
    },
    {
        "prezime": "Kovačević",
        "broj_kartice": "8765432187654321",
        "CVV": "456"
    },
    {
        "prezime": "Novak",
        "broj_kartice": "5555666677778888",
        "CVV": "789"
    }
]

async def secure_data(osjetljivi_podaci: dict):
    await asyncio.sleep(3)

    osigurani_podaci = {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': hash(str(osjetljivi_podaci['broj_kartice'])),
        'CVV': hash(str(osjetljivi_podaci['CVV']))
    }

    return osigurani_podaci

async def main():
    zadaci = []

    for zadatak in osjetljivi_podaci:
        zadatak = asyncio.create_task(secure_data(zadatak))
        zadaci.append(zadatak)

    rezultati = await asyncio.gather(*zadaci)

    print("Osigurani podaci:\n")
    for i, rezultat in enumerate(rezultati, 1):
        print(f"Osoba {i}:")
        print(f"Prezime: {rezultat['prezime']}")
        print(f"Broj kartice: {rezultat['broj_kartice']}")
        print(f"CVV: {rezultat['CVV']}")
        print()
    
    return rezultati

asyncio.run(main())



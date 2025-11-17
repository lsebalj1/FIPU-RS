import asyncio

async def dohvat_podataka():
    await asyncio.sleep(3)
    lista_brojeva = [x for x in range(1, 11)]
    print("Podaci dohvaćeni.")
    return lista_brojeva

async def main():
    rezultat = await dohvat_podataka()
    print(f"Podaci: {rezultat}")

if __name__ == "__main__":
    asyncio.run(main())
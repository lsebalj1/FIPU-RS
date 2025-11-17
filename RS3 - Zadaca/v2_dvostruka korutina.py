import asyncio
import time

async def dohvat_korisnika():
    print("Dohvacam korisnike")
    await asyncio.sleep(3)
    korisnici = [
        {"ime": "Ivan", "prezime": "Ivić", "godine": 25},
        {"ime": "Marko", "prezime": "Marković", "godine": 30},
        {"ime": "Ana", "prezime": "Anić", "godine": 22},
        {"ime": "Petra", "prezime": "Petrić", "godine": 28},
        {"ime": "Luka", "prezime": "Lukić", "godine": 35}
    ]
    print("Korisnici dohvaćeni.")
    return korisnici

async def dohvat_proizvoda():
    print("Dohvacam proizvode")
    await asyncio.sleep(5)
    proizvodi = [
        {"naziv": "Laptop", "cijena": 5000, "kategorija": "Elektronika"},
        {"naziv": "Miš", "cijena": 100, "kategorija": "Elektronika"},
        {"naziv": "Tipkovnica", "cijena": 200, "kategorija": "Elektronika"},
        {"naziv": "Monitor", "cijena": 1500, "kategorija": "Elektronika"},
        {"naziv": "Slušalice", "cijena": 300, "kategorija": "Audio"}
    ]
    print("Proizvodi dohvaceni")
    return proizvodi

async def main():
    rezultati = await asyncio.gather(
        dohvat_korisnika(), dohvat_proizvoda()
    )

    return rezultati

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvršavanja je {round(t2 - t1, 2)} sekundi")
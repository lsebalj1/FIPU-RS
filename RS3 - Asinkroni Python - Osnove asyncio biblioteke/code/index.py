import asyncio

# Definirajte korutinu secure_data koja simulira enkripciju
async def secure_data(osjetljivi_podaci):
    # Simuliramo enkripciju s hashiranjem
    await asyncio.sleep(3)  # Simulacija vremenskog trajanja enkripcije
    return {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': str(hash(osjetljivi_podaci['broj_kartice'])),
        'CVV': str(hash(osjetljivi_podaci['CVV']))
    }

# Lista osjetljivih podataka
osjetljivi_podaci_lista = [
    {'prezime': 'Ivanov', 'broj_kartice': '1234567890123456', 'CVV': '123'},
    {'prezime': 'Petrović', 'broj_kartice': '2345678901234567', 'CVV': '234'},
    {'prezime': 'Kovač', 'broj_kartice': '3456789012345678', 'CVV': '345'}
]

# Funkcija koja pokreće zadatke
async def main():
    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci_lista]
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat)

# Pokreni asinhroni zadatak
asyncio.run(main())

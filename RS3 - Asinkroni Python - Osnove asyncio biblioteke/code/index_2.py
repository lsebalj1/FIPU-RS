import asyncio
from typing import Coroutine
import time

# korutina je posebna vrsta funkcije koja koristi async def sintaksu i
# može koristiti await izraz unutar svog tijela

def sinkrona_funkcija(param: str) -> str:
    print("Ovo je sinkrona funkcija.")
    return param

nis = sinkrona_funkcija
print(nis)

async def korutina(param: int) -> int:
    return param

print(type(korutina))

nis_korutina = korutina(3)
print(type(nis_korutina))

objekt = korutina(4) # corutine object

async def korutina_2(vrijednost) -> int:
    return vrijednost

rezultat = asyncio.run(korutina_2(5)) # pozvali smo bez await
print(rezultat)

async def main():
    await korutina_2(10)

asyncio.run(main())

print(type(korutina_2(7)))

def funkcija():
    print("Pozvana je funkcija.")
    time.sleep(2) # I/O blokirajuća operacija blocking function
    print("Funkcija je završila.")
    return "Gotovo"

async def funkcija_asinkrona():
    print("Pozvana je asinkrona funkcija.")
    await asyncio.sleep(2) # I/O neblokirajuća operacija non-blocking function
    print("Asinkrona funkcija je završila.")
    return "Gotovo asinkrono"

#event loop je mehanizam koji upravlja izvršavanjem asinkronih funkcija i korutina

# GIL je mehanizam ua koji osigurava da samo jedna nit izvršava Python bytecode u jednom trenutku.

# konkuretno izvodenje je 

# Opercaijski sustav odlučuju koju nit ili proces dodijeliti CPU resurse u određenom trenutku vremena.

async def korutina_3():
    print("Korutina 3 počinje.")
    await asyncio.sleep(1)
    print("Korutina 3 završava.")
    return "Rezultat iz korutine 3"

asyncio.run(korutina_3())


#####################################################################
# Sekvencijalno izvodnje dvije funkcije koje simuliraju blokirajuće I/O operacije

def fetch_data(parametar):
    print("Delam nesto s parametrom:", parametar)
    time.sleep(parametar)
    return f"Rezultat za {parametar}"

def main_2():
    
    print("Izvršavanje main funkcije.")
    rezultat_1 = fetch_data(2)
    rezultat_2 = fetch_data(3)
    print("Zavravanje main  funkcije.")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
main_2()
t2 = time.perf_counter()

print(f"Vrijeme izvršavanja je {round(t2 - t1, 2)} sekundi")

# Event loop za ovaj kod je blokiran tijekom izvođenja fetch_data funkcija koje simuliraju
# EVENT LOOP JE BLOKIRAN:
# fetch_data(2) --> čeka 2 sekunde (program ne radi ništa drugo)
# fetch_data(3) --> čeka 3 sekunde (program ne radi ništa drugo)
# Ukupno: 5 sekundi jer se izvršavaju sekvencijalno

# background IO su blokirajuće operacije.


async def async_fetch_data(parametar):
    print("Delam nesto s parametrom:", parametar)
    await asyncio.sleep(parametar)
    return f"Rezultat za {parametar}"

async def async_main_2():
    print("Izvršavanje main funkcije.")
    rezultat_3 = async_fetch_data(2)
    rezultat_4 = async_fetch_data(3)
    print("Zavravanje main funkcije.")
    return rezultat_3, rezultat_4

t3 = time.perf_counter()
asyncio.run(async_main_2())
t4 = time.perf_counter()

print(f"Vrijeme izvršavanja je {round(t4 - t3, 2)} sekundi")

# Event loop nije blokiran tijekom izvođenja async_fetch_data funkcija koje simuliraju

# event loop prikaz:
# fetch_data(2) --> čeka 2 sekunde
# fetch_data(3) --> čeka 3 sekunde
# main funkcija čeka da obje završe


# background IO neblokirajuće operacije.
# time.perf_counter() mjeri vrijeme izvršavanja koda.

# PROBLEM: Ovaj kod je još uvijek sekvencijalan jer koristimo 'await' odmah!


#####################################################################
# Konkuretno izvodnje dvije korutine koristeći asyncio.create_task()

async def fetch_data_konkuretno(parametar):
    print("Delam nesto s parametrom:", parametar)
    await asyncio.sleep(parametar)
    return f"Rezultat za {parametar}"

async def main_konkuretno():
    print("Izvršavanje main funkcije.")
    task1 = asyncio.create_task(fetch_data_konkuretno(2)) # schedule
    task2 = asyncio.create_task(fetch_data_konkuretno(3)) # schedule
    
    rezultat_1 = await task1 #run
    rezultat_2 = await task2 #run
    
    print("Zatvaranje main funkcije.")
    return rezultat_1, rezultat_2

t5 = time.perf_counter()
asyncio.run(main_konkuretno())
t6 = time.perf_counter()
print(f"Vrijeme izvršavanja je {round(t6 - t5, 2)} sekundi")

# Event Loop
# fetch_data(2) --> čeka 2 sekunde
# fetch_data(3) --> čeka 3 sekunde
# Ukupno: 3 sekunde jer se izvršavaju konkuretno
# To znači da dok jedna korutina čeka, druga može koristiti CPU resurse.

# PROBLEM: Ovaj kod koristi asyncio.create_task() što može biti loše za više taskova.
# jer stvara puno taskova koji se moraju pratiti.

#####################################################################
# Konkuretno izvodnje dvije korutine koristeći asyncio.gather()

async def fetch_data_gather(parametar):
    print("Delam nesto s parametrom:", parametar)
    await asyncio.sleep(parametar)
    return f"Rezultat za {parametar}"

async def main_gather():
    print("Izvršavanje main funkcije.")
    rezultati = await asyncio.gather(
        fetch_data_gather(2),
        fetch_data_gather(3)
    )
    print("Zatvaranje main funkcije.")
    return rezultati

t7 = time.perf_counter()
asyncio.run(main_gather())
t8 = time.perf_counter()
print(f"Vrijeme izvršavanja je {round(t8 - t7, 2)} sekundi")


import aiohttp
import asyncio
import requests
import time

# sinkorono slanje podatka

response = requests.get("https://catfact.ninja/fact")

print(response)

print(response.text)

print(type(response.text))

print(response.text[2])

#deserijalizacija

print(response.json())

print(type(response.json()))

def send_request():
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json()["fact"]
    print(fact)

start_time = time.time()

for i in range(1, 6):
    print(f"\nŠaljemo {i}. zahtjev")
    send_request()
    
end_time = time.time()

print(f"\nVrijeme izvrsavanja sinkronog je {end_time - start_time:.2f}")

# problem kod sekvencijalnog tj sinkronog je sto kod puno
# zahtjeva program traje dugo

# asinkrono programiranje
#CLIENT SESSION 

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        
        for i in range(1, 6):
            print(f"\nŠaljemo {i}. zahtjev")
            response = await session.get("https://catfact.ninja/fact")
            response_json = await response.json()
            print(response_json["fact"])
        print("GOtovo")
        end_time = time.time()
        print(f"\nVrijeme izvrsavanja Asinkronog je {end_time - start_time:.2f}")
        
        
asyncio.run(main())        
        
# problem: jos uvijek svaki zahtjev ceka na izvrsenje prijasnjeg    
    
# konkuretno slanje
# Slanje konkurentnih zahtjeva kroz asyncio.gather

async def get_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    response_json = await response.json()
    return response_json

async def main_2():
    start_time = time.time()
    print("Šaljemo zahtjev")
    async with aiohttp.ClientSession() as session_2:
        liste_korutina = [get_fact(session_2) for i in range(1, 6)]
        rezultati = await asyncio.gather(*liste_korutina)
        print(rezultati)
        end_time = time.time()
        print(f"\nVrijeme izvrsavanja Asinkronog kroz asyncio.gather je {end_time - start_time:.2f}")
        
        
asyncio.run(main_2()) 

# ne izvrsavaju se istovremeno, 
# npr fact zahtjev 4 moze doci prije fact 2
# konkuretni kod je 80% brzi      

# Slanje konkurentnih zahtjev kroz asynio.tasks

async def main_3():
    start_time = time.time()
    print("Šaljemo zahtjev")
    async with aiohttp.ClientSession() as session_3:
        taskovi = [asyncio.create_task(get_fact(session_3)) for i in range(1, 6)]
        rezultati = await asyncio.gather(*taskovi)
        print(rezultati)
        end_time = time.time()
        print(f"\nVrijeme izvrsavanja Asinkronog kroz asynio.tasks je {end_time - start_time:.2f}")
        
        
asyncio.run(main_3()) 
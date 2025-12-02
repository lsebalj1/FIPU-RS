import time
import asyncio
import aiohttp
import requests

def zadatak(sekunde: int) -> str:
    time.sleep(sekunde)
    return f"Zadatak završen nakon {sekunde} sekundi."

async def asinkroni_zadatak(sekunde: int) -> str:
    await asyncio.sleep(2)
    return f"Zadatak završen nakon {sekunde} sekundi."

def main():
    print(zadatak(3))
    print(zadatak(2))
    print(zadatak(1))
    
main()

async def async_main():
    
    rezultati = await asyncio.gather(
        asinkroni_zadatak(3), 
        asinkroni_zadatak(2),
        asinkroni_zadatak(1)
    )
    
    return rezultati

t1 = time.perf_counter()
asyncio.run(async_main())
t2 = time.perf_counter() 
print(f"Vrijeme izvrsavanja {t2 - t1} sekundi")   

async def async_main_bez_gather():
    task1 = asyncio.create_task(asinkroni_zadatak(3))
    task2 = asyncio.create_task(asinkroni_zadatak(2))
    task3 = asyncio.create_task(asinkroni_zadatak(1))
    
    rezultat1 = await task1 
    rezultat2 = await task2
    rezultat3 = await task3
    
    print(rezultat1)
    print(rezultat2)
    print(rezultat3)

t3 = time.perf_counter()
asyncio.run(async_main_bez_gather())
t4 = time.perf_counter() 
print(f"Vrijeme izvrsavanja {t4 - t3} sekundi") 

def posalji_zahtjev(url: str) -> dict:
    response = requests.get(url) 
    return response.json()  

def sinkrono_main():
    start_time = time.time()
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    titles = []
    
    for _ in range(3):
        data = posalji_zahtjev(url)
        titles.append(data["title"])
    
    end_time = time.time()
    
    print(f"Titles: {titles}")
    print(f"Ukupno vrijeme: {end_time - start_time}")
    
sinkrono_main() 

async def asinkroni_posalji_zahtjev(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def asinkrono_main():
    start_time = time.time()
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    tasks = [asinkroni_posalji_zahtjev(url) for _ in range(3)]
    
    result = await asyncio.gather(*tasks)
    
    titles = [r["title"] for r in result]
    
    end_time = time.time()
    
    print(f"Titles: {titles}")
    print(f"Ukupno vrijeme: {end_time - start_time}")
    
asyncio.run(asinkrono_main())  
    
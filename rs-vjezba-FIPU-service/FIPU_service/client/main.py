import asyncio
import aiohttp 

URL = "http://127.0.0.1:8000"

async def get_student(session):
    async with session.get(f"{URL}/studenti") as response:
        data = await response.json()
        print("GEt studenti status {response.status}")
        return data

async def get_kolegij(session):
    async with session.get(f"{URL}/kolegiji") as response:
        data = await response.json()
        print("Get kolegij status {response.status}")
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        student_tasks = [get_student(session) for _ in range(50)]
        kolegij_tasks = [get_kolegij(session) for _ in range(30)]
    
        all_tasks = student_tasks + kolegij_tasks
        
        results = await asyncio.gather(*all_tasks)
        
        print(f"Ukupno poslano zahtjeva {len(results)}")
    
asyncio.run(main())
        
    

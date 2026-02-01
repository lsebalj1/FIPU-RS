from aiohttp import web
import asyncio

URL = "http://127.0.0.1:8000"

async def get_user_by_id(session):
    async with session.get(f"{URL}/users/{id}") as response:
        data = await response.json()
        return data

async def get_user_by_username(session):
    async with session.get("{URL}/users/{username}") as reposnse:
        data = await reposnse.json()
        return data

async def main():
    async with aiohttp.ClientSession() as session: 
        users_id_task = [get_user_by_id(session) for _ in range(70)]
        users_username_task = [get_user_by_username(session) for _ in range(50)]
        
        all_tasks = users_id_task + users_username_task
        
        results = asyncio.gather(*all_tasks)
        
        print(results)

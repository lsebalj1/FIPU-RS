from aiohttp import web
import asyncio
import datetime

messages = []

async def send_message(request): 
    sender = request.match_info[request]
    receiver = request.match_info[request]
    
    data = await response.json()
    content = data.get('content', '')
    
    message = {
        "timestamp" : datetime.now().isoformat(),
        "content" : content,
        "sender" : sender,
        "receiver" : receiver
    }
    
    messages.append(message)
    
    return web.json_response(message, status = 200)

app = web.Application()

app.router.add_post("/message/{sender}/{receiver}", send_message)

async def start_server(): 
    runner = web.AppRunner(app) 
    await runner.setup() 
    host = "localhost"
    port = 9000
    site = web.TCPSite(runner, host, port) 
    await site.start() 

async def main():
    asyncio.create_task(start_server())
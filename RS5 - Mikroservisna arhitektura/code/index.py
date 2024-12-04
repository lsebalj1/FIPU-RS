from aiohttp import web
import asyncio

async def notify(request):
    data = await request.json()
    print(f"Notification sent: {data}")
    return web.Response(text="Notification sent!")

app = web.Application()
app.router.add_post('/notify', notify)

if __name__ == "__main__":
    web.run_app(app, port=8003)

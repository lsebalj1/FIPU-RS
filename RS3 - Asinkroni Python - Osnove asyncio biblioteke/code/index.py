import asyncio
import time

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')
    return name, True

async def main():
  
  timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
  
  # 1. način
  await timers[0]
  await timers[1]
  await timers[2]
  
  # 2. način
  
  for timer in timers:
    await timer
    
  # 3. način
  
  lista_rezultata = [await timer for timer in timers]
  
  # 4. način
  
  await asyncio.gather(*timers)

asyncio.run(main())
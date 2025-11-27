import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
        print(f'{name}: Vrijeme je isteklo!')

async def main():
    # Kreiranje taskova - sva 3 su zakazana u event loop queue
    timers = [
        # create_task() zakazuje task
        asyncio.create_task(timer('Timer 1', 3)),  
        asyncio.create_task(timer('Timer 2', 5)),  
        asyncio.create_task(timer('Timer 3', 7)) 
    ]
    
    # await gather() - main() čeka dok nisu svi taskovi gotovi, event loop preuzima kontrolu
    
    await asyncio.gather(*timers)  
    
    # ITERACIJA 1 - Event loop pokreće taskove redom
    # Sva 3 taska su u waiting mode
    # Sva 3 taska čekaju 1 sekundu paralelno
    
    # ITERACIJA 2 - Event loop budi taskove nakon sleep 1 sekundu
    
    # ITERACIJE 3+
    # Svake sekunde event loop budi sve aktivne taskove
    # Isti proces se ponavlja svake sekunde
    # Kad je task gotov više se ne izvršava
    # gather () Čeka dok svi ne budu gotovi
    # main() završava, event loop se zatvara

# Pokreće event loop i main() korutinu
asyncio.run(main())  

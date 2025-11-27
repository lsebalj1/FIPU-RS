import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) 
    task2 = asyncio.create_task(fetch_data(2)) 
    rezultati = await asyncio.gather(task1, task2)
    print("Fetch 1 i 2 uspješno završeni.")
    return rezultati

t1 = time.perf_counter()
rezultati = asyncio.run(main()) 
t2 = time.perf_counter()
print(rezultati)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
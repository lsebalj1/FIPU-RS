import asyncio
import aiohttp
import time

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']

async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    response = await session.get(url)
    data = await response.json()
    
    # Extract the dog fact from the response
    dog_fact = data.get("data", [])[0].get("attributes", {}).get("body", "")
    return dog_fact

def mix_facts(dog_facts, cat_facts):
    mixed_facts = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)
    return mixed_facts

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
        
        results = await asyncio.gather(
            *dog_facts_tasks,
            *cat_facts_tasks
        )
        
        dog_facts = results[:5]
        cat_facts = results[5:]

        filtered_facts = mix_facts(dog_facts, cat_facts)
        
        print("Filtered Facts:")
        for fact in filtered_facts:
            print(fact)

    end = time.time()

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())

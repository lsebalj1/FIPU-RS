import asyncio
import time
from datetime import datetime
import random

async def get_camera_data(camera_id: int) -> dict:
    await asyncio.sleep(random.uniform(0.1, 5))
    
    await asyncio.sleep(0.5)
    
    camera_data = {
        "camera_id": camera_id,
        "timestamp": datetime.now().isoformat(),
        "vehicle_count":  random.randint(5, 20) 
    }
    
    return camera_data
        
async def main():
    start_time = time.time()
    
    camera_ids = [1, 2, 3, 4, 5]
    
    tasks = [get_camera_data(camera_id) for camera_id in camera_ids]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    ukupno_vrijeme = round(end_time - start_time, 2)
    
    print("Podaci s kamera:")
    for result in results:
        print(f"Kamera {result['camera_id']}: {result['vehicle_count']} vozila @ {result['timestamp']}")
    
    ukupno_vozila = sum(result['vehicle_count'] for result in results)
    prosjek_vozila = round(ukupno_vozila / len(results), 2)
    
    print(f"\nProsječan broj vozila: {prosjek_vozila}")
    print(f"Ukupno vrijeme izvođenja: {ukupno_vrijeme} sekundi")

if __name__ == "__main__":
    asyncio.run(main())
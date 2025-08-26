import asyncio
import random

async def download_file(file_name):
    print(f"Starting download: {file_name}")
    
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"Finished download: {file_name} in {delay} seconds")
    return file_name

async def main():
    files = [f"file{i}.txt" for i in range(1, 6)]
    tasks = [download_file(file) for file in files]
    results = await asyncio.gather(*tasks)
    print("All files downloaded:", results)

asyncio.run(main())

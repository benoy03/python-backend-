import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    print("All fetches completed.")


asyncio.run(main())

# Complete Project Code
import asyncio
import aiohttp
import time

API_URLS = {
    "Users": "https://jsonplaceholder.typicode.com/users",
    "Posts": "https://jsonplaceholder.typicode.com/posts",
    "Comments": "https://jsonplaceholder.typicode.com/comments"
}

semaphore = asyncio.Semaphore(2)


async def fetch_api(session, name, url):
    async with semaphore:

        for attempt in range(1, 4):
            try:
                print(f"Fetching {name}... Attempt {attempt}")

                async with asyncio.timeout(5):
                    async with session.get(url) as response:
                        response.raise_for_status()
                        data = await response.json()

                        return {
                            "name": name,
                            "status": "Success",
                            "count": len(data)
                        }

            except (aiohttp.ClientError, asyncio.TimeoutError) as error:
                print(f"{name} failed: {error}")

                if attempt == 3:
                    return {
                        "name": name,
                        "status": "Failed",
                        "count": 0
                    }

                await asyncio.sleep(2 ** (attempt - 1))


async def main():
    start_time = time.perf_counter()

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        tasks = [
            fetch_api(session, name, url)
            for name, url in API_URLS.items()
        ]

        results = await asyncio.gather(*tasks)

    print("\n========== API DASHBOARD ==========")

    for result in results:
        print(f"\nAPI: {result['name']}")
        print(f"Status: {result['status']}")
        print(f"Records: {result['count']}")

    end_time = time.perf_counter()

    print("\n===================================")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

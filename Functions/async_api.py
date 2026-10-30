# Real world API Example Full code .
# import asyncio
# import aiohttp

# BASE_URL = "https://jsonplaceholder.typicode.com"


# async def fetch_data(session, url):
#     """Fetch JSON data from an API endpoint."""

#     try:
#         async with session.get(url) as response:
#             response.raise_for_status()
#             data = await response.json()

#             print(f"Success: {url}")
#             return data

#     except (aiohttp.ClientError, asyncio.TimeoutError) as error:
#         print(f"API Error: {url}")
#         print(f"Reason: {error}")
#         return None


# async def main():
#     timeout = aiohttp.ClientTimeout(total=15)

#     async with aiohttp.ClientSession(timeout=timeout) as session:

#         # Create multiple API tasks
#         user_task = asyncio.create_task(
#             fetch_data(session, f"{BASE_URL}/users/1")
#         )

#         post_task = asyncio.create_task(
#             fetch_data(session, f"{BASE_URL}/posts/1")
#         )

#         posts_task = asyncio.create_task(
#             fetch_data(session, f"{BASE_URL}/posts?userId=1")
#         )

#         # Wait for all three requests
#         user, post, posts = await asyncio.gather(
#             user_task,
#             post_task,
#             posts_task
#         )

#         # Display user information
#         print("\n========== USER DETAILS ==========")

#         if user is not None:
#             print("Name:", user["name"])
#             print("Email:", user["email"])
#             print("City:", user["address"]["city"])

#         # Display single post
#         print("\n========== SINGLE POST ==========")

#         if post is not None:
#             print("Title:", post["title"])
#             print("Body:", post["body"])

#         # Display multiple posts
#         print("\n========== USER POSTS ==========")

#         if posts is not None:
#             print("Total posts:", len(posts))

#             for item in posts[:5]:
#                 print(f"\nPost ID: {item['id']}")
#                 print("Title:", item["title"])


# if __name__ == "__main__":
#     asyncio.run(main())
# 
# 


# Async Code to test Perfomance
# import asyncio
# import time


# async def task(name, seconds):
#     print(f"{name} started")

#     await asyncio.sleep(seconds)

#     print(f"{name} completed")


# async def main():
#     start = time.perf_counter()

#     await asyncio.gather(
#         task("Task A", 2),
#         task("Task B", 3),
#         task("Task C", 1)
#     )

#     end = time.perf_counter()

#     print(f"Total time: {end - start:.2f} seconds")


# asyncio.run(main())


# Async Debugging with debug mode
# import asyncio


# async def say_hello():
#     await asyncio.sleep(1)
#     print("Hello from asyncio!")


# async def main():
#     await say_hello()


# asyncio.run(main(), debug=True)
# 
# 


# Async functions testing with unittest
# 
# import asyncio
# import unittest


# async def add_async(a, b):
#     await asyncio.sleep(0.1)
#     return a + b


# async def fetch_user(user_id):
#     await asyncio.sleep(0.1)

#     return {
#         "id": user_id,
#         "name": "Anshul"
#     }


# class TestAsyncFunctions(unittest.IsolatedAsyncioTestCase):

#     async def test_add_async(self):
#         result = await add_async(10, 20)

#         self.assertEqual(result, 30)

#     async def test_fetch_user(self):
#         user = await fetch_user(1)

#         self.assertEqual(user["id"], 1)
#         self.assertEqual(user["name"], "Anshul")


# if __name__ == "__main__":
#     unittest.main()
# 
# 


# Mocking Async Functions — AsyncMock
# import asyncio
# from unittest.mock import AsyncMock

# async def main():
#     fetch_user = AsyncMock(
#         return_value={"id": 1, "name": "Anshul"}
#     )

#     user = await fetch_user(1)

#     print(user)
#     print(fetch_user.await_count)

# asyncio.run(main())
# 
# 



# Robust Async API Client
# import asyncio
# import random
# import aiohttp

# BASE_URL = "https://jsonplaceholder.typicode.com"

# MAX_CONCURRENT_REQUESTS = 3
# MAX_ATTEMPTS = 3
# REQUEST_TIMEOUT = 5

# semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)


# async def fetch_json(session, url):
#     async with semaphore:
#         for attempt in range(1, MAX_ATTEMPTS + 1):
#             try:
#                 async with asyncio.timeout(REQUEST_TIMEOUT):
#                     async with session.get(url) as response:

#                         if response.status == 429:
#                             retry_after = response.headers.get(
#                                 "Retry-After"
#                             )

#                             if attempt == MAX_ATTEMPTS:
#                                 response.raise_for_status()

#                             delay = (
#                                 float(retry_after)
#                                 if retry_after
#                                 else 2 ** (attempt - 1)
#                             )

#                             print(
#                                 f"Rate limited. Waiting {delay}s..."
#                             )

#                             await asyncio.sleep(delay)
#                             continue

#                         if response.status in (500, 502, 503, 504):
#                             if attempt == MAX_ATTEMPTS:
#                                 response.raise_for_status()

#                             delay = (
#                                 2 ** (attempt - 1)
#                                 + random.uniform(0, 0.5)
#                             )

#                             print(
#                                 f"Server error {response.status}. "
#                                 f"Retrying in {delay:.2f}s"
#                             )

#                             await asyncio.sleep(delay)
#                             continue

#                         response.raise_for_status()
#                         return await response.json()

#             except (aiohttp.ClientError, TimeoutError) as error:
#                 if attempt == MAX_ATTEMPTS:
#                     print(f"Request failed: {url}")
#                     print(f"Reason: {error}")
#                     return None

#                 delay = (
#                     2 ** (attempt - 1)
#                     + random.uniform(0, 0.5)
#                 )

#                 print(
#                     f"Attempt {attempt} failed. "
#                     f"Retrying in {delay:.2f}s"
#                 )

#                 await asyncio.sleep(delay)

#     return None


# async def get_user(session, user_id):
#     return await fetch_json(
#         session,
#         f"{BASE_URL}/users/{user_id}"
#     )


# async def get_posts(session, user_id):
#     return await fetch_json(
#         session,
#         f"{BASE_URL}/posts?userId={user_id}"
#     )


# async def get_todos(session, user_id):
#     return await fetch_json(
#         session,
#         f"{BASE_URL}/todos?userId={user_id}"
#     )


# async def main():
#     timeout = aiohttp.ClientTimeout(total=15)

#     async with aiohttp.ClientSession(
#         timeout=timeout
#     ) as session:

#         results = await asyncio.gather(
#             get_user(session, 1),
#             get_posts(session, 1),
#             get_todos(session, 1)
#         )

#     user, posts, todos = results

#     print("\n========== API RESULTS ==========")

#     if user is not None:
#         print("User:", user["name"])
#         print("Email:", user["email"])
#     else:
#         print("User request failed.")

#     if posts is not None:
#         print("Posts received:", len(posts))
#     else:
#         print("Posts request failed.")

#     if todos is not None:
#         print("Todos received:", len(todos))
#     else:
#         print("Todos request failed.")


# if __name__ == "__main__":
#     asyncio.run(main())

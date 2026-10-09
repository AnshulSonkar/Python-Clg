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
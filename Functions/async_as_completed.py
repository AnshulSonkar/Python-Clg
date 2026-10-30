# import asyncio

# async def fetch_data(name, delay):
#     print(f"Starting {name}...")

#     await asyncio.sleep(delay)

#     return f"{name} completed after {delay} seconds"


# async def main():
#     tasks = [
#         fetch_data("Users API", 3),
#         fetch_data("Products API", 1),
#         fetch_data("Orders API", 2)
#     ]

#     for task in asyncio.as_completed(tasks):
#         result = await task
#         print(result)


# asyncio.run(main())



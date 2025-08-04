import asyncio
from time import sleep
# async def Hello_World(word):
#     await asyncio.sleep(1)
#     print(word)

# asyncio.run(Hello_World("Hello World"))

# async def main():
#     await asyncio.gather(
#         Hello_World("Hello World"),
#         Hello_World("Hello World"),
#     )

# asyncio.run(main())


async def sayHello(word):
    sleep(4)
    print(word)

async def main():
    await asyncio.gather(
        sayHello("Hello Line 2"),
    )

asyncio.run(main())


print("Hello Line 1")
asyncio.run(sayHello("Hello Line 2"))
print("Hello Line 3")
print("Hello Line 4")
print("Hello Line 5")


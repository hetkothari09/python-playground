import asyncio
import redis.asyncio as redis

'''
using async redis option, we can handle or run multiple requests on the server without blocking the entire server for just 1 request
This helps in achieving execution of parallel tasks
'''

async def get_set():
    r = redis.Redis(
        host='localhost',
        port=6379,
        db=0
    )

    await r.set("my_async_variable:1", "Hi")
    await r.set("my_async_variable:2", "How")
    await r.set("my_async_variable:3", "are")
    await r.set("my_async_variable:4", "you")

    value1 = await r.get("my_async_variable:1")
    value2 = await r.get("my_async_variable:2")

    print(value1.decode())
    print(value2.decode())

    await r.close()

if __name__ == '__main__':
    asyncio.run(get_set())

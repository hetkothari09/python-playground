import asyncio
import redis.asyncio as redis

async def time_to_live():
    r = redis.Redis(host='localhost', port=6379, db=0)

    await r.setex("my_expiry_variable", 10, "Hey")

    value = await r.get("my_expiry_variable")
    print(value.decode())

    await asyncio.sleep(11)
    expired_value = await r.get("my_expiry_variable")
    print(expired_value)
    await r.aclose()


if __name__ == '__main__':
    asyncio.run(time_to_live())
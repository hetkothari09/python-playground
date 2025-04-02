import redis

r = redis.Redis(
    host='localhost',
    port='6379',
    db=0
)

r.lpush('food', 'Pizza')
r.rpush('food', 'Burger')
r.lpush('food', 'Pasta')
r.rpush('food', 'Nachos')

r.lpop('food')
r.rpop('food')

print((r.lrange('food', 0, 10)))

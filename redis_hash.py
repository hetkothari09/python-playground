import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

r.hset("user:1", "name", "Het")
r.hset("user:1", "email", "hetkothari@gmail.com")
r.hset("user:1", "major", "computer science")

email = r.hget("user:1", "email")

print(email.decode())
print(r.hgetall("user:1"))

r.hdel("user:1", "major")

print(r.hgetall("user:1"))

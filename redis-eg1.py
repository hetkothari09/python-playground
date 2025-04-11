import redis

r = redis.Redis(
    host='localhost',
    port='6379',
    db=0,
    password='root'
)

# r.auth(password="root")
r.set('windows_key', "Hello from windows (python)")
value = r.get('windows_key')
print(value)
print(value.decode())


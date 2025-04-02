from audioop import minmax

import redis

r = redis.Redis(
    host = 'localhost',
    port = 6379,
    db = 0
)

def create_user_profile(user_id, name, email):
    user_key = f'user:{user_id}'
    r.hset(user_key, mapping={"name": name, "email": email})
    print(f"User {user_id}'s profile created")

def get_user_profile(user_id):
    user_key = f"user:{user_id}"
    values = r.hgetall(user_key)
    print(f"user:{user_id}")
    print({i.decode(): k.decode() for i, k in values.items()})

def delete_user_profile(user_id):
    print("Deleting user profile....")
    user_key = f"user:{user_id}"
    r.delete(user_key)
    print(f"User: {user_id}'s profile deleted!")

if __name__ == '__main__':
    create_user_profile(100, "Het", "hetkothari@gmail.com")
    create_user_profile(101, "Test", "test@gmail.com")

    get_user_profile(100)
    get_user_profile(101)

    delete_user_profile(101)
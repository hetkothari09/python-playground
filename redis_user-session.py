import redis

r = redis.Redis(
    host = 'localhost',
    port = 6379,
    db = 0
)

def start_user_session(user_id, token, ttl=10):
    user_key = f"user:{user_id}:token"
    r.setex(user_key, ttl, token)
    print(f"Started user session for user:{user_id}....")

def get_user_session_token(user_id):
    user_key = f"user:{user_id}:token"
    token_value = r.get(user_key)

    print({token_value.decode() if token_value else None})

if __name__ == '__main__':
    # start_user_session(10, "xyz_session-token_xyz")
    get_user_session_token(10)
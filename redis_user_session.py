import redis
import uuid

r = redis.Redis(
    host='localhost',
    port='6379',
    db=0,
    password='root'
)

def create_user_session(user_id):
    session_key = f'user:{user_id}:session'

    # generates a random token
    token = str(uuid.uuid4())
    r.set(session_key, token)
    return {"session created successfully" : token}


def get_user_session(user_id):
    session_key = f'user:{user_id}:session'
    token = r.get(session_key)
    return {"Got the user session": token.decode()}

def delete_user_session(user_id):
    session_key = f'user:{user_id}:session'
    token = r.delete(session_key)
    return {"Session deleted successfully": token}

if __name__ == '__main__':
    session_user1 = create_user_session(100)
    print(session_user1)

    get_user1 = get_user_session(100)
    print(get_user1)

    # delete_user1 = delete_user_session(100)
    # print(delete_user1)

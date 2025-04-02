import redis
import requests
import json
import time

r = redis.Redis(
    host='localhost',
    port = 6379,
    db = 0
)

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
data = response.json()

# data = json.dumps(response.json())
# print(data)

# for i in data:
#     if i["userId"] == 1:
#         print(i)
#     else:
#         pass

'''
Here I first check the user data in the cache, then if the data is found in the cache, then it returns it
or else it makes the api call, then fetches the data from the api and then stores it in the redis as a cache
and sets an expiry of 10 seconds to it. So the next time if the data is fetched before the expiry timing
then it returns the data from the cache.
'''


def get_user_data(user_id):
    cache_key = f"userId:{ user_id}"
    cache_data = r.get(cache_key)

    if cache_data:
        start_time = time.time()
        print("Found data in cache...")
        print(json.loads(cache_data))
        end_time = time.time()
        print(f"Time taken = {end_time-start_time}")

    else:
        start_time = time.time()
        print("Cache for the data not found...Fetching from an API....")

        for i in data:
            if i['userId'] == user_id:
                values = i
                print(i)
                r.setex(cache_key, 10, json.dumps(values))
                break
        end_time = time.time()
        print(f"Time taken = {end_time-start_time}")

if __name__ == '__main__':
    get_user_data(2)



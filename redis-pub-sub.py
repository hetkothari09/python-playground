import redis
import threading
import time

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

def subscriber(r, channel_name):
    pubsub = r.pubsub()
    pubsub.subscribe(channel_name)
    print(f'Subscribed to {channel_name}')

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Message: {message['data'].decode()}")

def publisher(r, channel_name, message):
    r.publish(channel_name, message)

if __name__ == '__main__':
    channel = "updates"
    sub_thread = threading.Thread(target=subscriber, args=(r, channel))
    sub_thread.start()

    time.sleep(5)
    # publisher(r, channel, "Welcome to Het's Messaging Service!")
    publisher(r, channel, "Welcome to Het's Messaging Service!")
    publisher(r, channel, "So How are you!")
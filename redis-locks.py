import redis
import time

from redis.exceptions import LockError

r = redis.Redis(
    host = 'localhost',
    port = 6379,
    db = 0
)

def critical_section_simulation():
    lock = r.lock("imp-resource", timeout=20)

    try:
        acquire = lock.acquire(blocking=True, blocking_timeout=5)
        if acquire:
            print("Acquired the lock for a critical operation!")
            time.sleep(10)
        else:
            print("Failed to acquire the lock for 5 seconds!")
    except LockError:
        print("Lock is already acquired! Please try again later!")
    finally:
        lock.release()

if __name__ == '__main__':
    critical_section_simulation()
import time

def cache_func(func):
    cache_value = {}
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        return result
    return wrapper

@cache_func
def add(a,b):
    time.sleep(5)
    return a + b

if __name__ == '__main__':
    print(add(10, 9))
    print(add(10, 9))
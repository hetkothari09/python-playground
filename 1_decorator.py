import time

# Here timer function acts like a toll booth. It accepts a function as an argument. Then there is a wrapper
# function that is basically the toll booth which calculates time and prints the result.
# Then when you use this timer function as a decorator @timer, then that function should be passed through
# the timer function compulsory like a toll booth.

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time-start_time} to execute.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)


if __name__ == '__main__':
    example_function(4)
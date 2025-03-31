def decorator_func(func):
    def wrapper(*args, **kwargs):
        # for arg in args:
        #     print(arg)
        # for kwarg in kwargs:
        #     print(kwarg)
        args_value = ', '.join(arg for arg in args)
        kwargs_value = ', '.join(v for k, v in kwargs.items())
        print(f"The function {func.__name__} has args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@decorator_func

def hello():
    print("Hello")

@decorator_func
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

if __name__ == '__main__':
    hello()
    greet("Het", greeting="Kemcho")
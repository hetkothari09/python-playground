import logging
from functools import wraps

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_function(func):
    """Decorator to log function calls and exceptions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function {func.__name__} called with args: {args} kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function {func.__name__} returned {result}")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
            raise
    return wrapper

# Apply decorator to functions
@log_function
def divide(a, b):
    return a / b

@log_function
def greet(name):
    return f"Hello, {name}"

# Testing
greet("Alice")
divide(10, 2)
divide(5, 0)  # This will log the exception

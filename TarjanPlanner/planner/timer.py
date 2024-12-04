import time
import functools
import logging

# Configure logging
logging.basicConfig(
    filename='execution_time_TarjanPlanner.log',
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def timeit(func):
    """
    Decorator to measure the execution time of a function and log it.
    Returns a tuple: (result, elapsed_time)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        # Log the execution time
        logging.info(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        # No print statement here
        return result, elapsed_time  # Return both result and elapsed time
    return wrapper

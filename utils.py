import time

def measure_execution_time(func):
    """
    Decorator to measure the execution time of a function.

    :param func: The function to be measured.
    :return: The wrapped function with execution time measurement.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result

    return wrapper


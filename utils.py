import time
import tracemalloc

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

def measure_memory_usage(func):
    """
    Decorator to measure the memory usage of a function.

    :param func: The function to be measured.
    :return: The wrapped function with memory usage measurement.
    """
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage of {func.__name__}: {current / 10**6:.6f} MB; Peak: {peak / 10**6:.6f} MB")
        return result

    return wrapper


from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    def decorator(func):
        # Create cache as OrderedDict to maintain LRU order
        cache = OrderedDict()
        # Store timestamps for each key
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args and kwargs
            key = str(args)
            if kwargs:
                key += str(sorted(kwargs.items()))
            if typed:
                key += str(tuple(type(arg) for arg in args))
                if kwargs:
                    key += str(tuple(type(val) for val in kwargs.values()))

            current_time = timer()

            # Check if key exists and hasn't expired
            if key in cache:
                if current_time - timestamps[key] < ttl:
                    # Move accessed item to end (most recently used)
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    # Remove expired item
                    del cache[key]
                    del timestamps[key]

            # Compute new value
            result = func(*args, **kwargs)

            # Remove oldest item if cache is full
            if maxsize > 0 and len(cache) >= maxsize:
                oldest = next(iter(cache))
                del cache[oldest]
                del timestamps[oldest]

            # Add new value to cache
            cache[key] = result
            timestamps[key] = current_time
            return result

        # Add cache clear method
        def clear_cache():
            cache.clear()
            timestamps.clear()

        wrapper.clear_cache = clear_cache
        return wrapper

    return decorator
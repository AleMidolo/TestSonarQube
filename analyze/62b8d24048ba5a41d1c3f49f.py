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
        # Create cache as ordered dictionary
        cache = OrderedDict()
        # Store timestamps for each key
        timestamps = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on arguments
            key = str(args)
            if kwargs:
                key += str(sorted(kwargs.items()))
            if typed:
                key += str(tuple(type(arg) for arg in args))
                if kwargs:
                    key += str(tuple(type(val) for val in kwargs.values()))

            # Get current time
            now = timer()

            # Check if key exists and hasn't expired
            if key in cache:
                if now - timestamps[key] < ttl:
                    # Move to end to mark as recently used
                    cache.move_to_end(key)
                    return cache[key]
                else:
                    # Remove expired item
                    del cache[key]
                    del timestamps[key]

            # Compute new value
            result = func(*args, **kwargs)

            # Add to cache
            cache[key] = result
            timestamps[key] = now

            # Remove oldest items if cache is too large
            while len(cache) > maxsize:
                oldest_key = next(iter(cache))
                del cache[oldest_key]
                del timestamps[oldest_key]

            return result

        # Add clear method to wrapper
        def clear_cache():
            cache.clear()
            timestamps.clear()

        wrapper.clear_cache = clear_cache
        return wrapper

    return decorator
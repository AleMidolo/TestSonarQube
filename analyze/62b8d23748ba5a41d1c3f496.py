from collections import defaultdict
import functools

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Cache to store function results
        cache = {}
        # Counter to track frequency of key access
        freq_counter = defaultdict(int)
        # Track order of insertion for same frequency items
        insertion_order = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args and kwargs
            key = (*args, *(sorted(kwargs.items())))
            if typed:
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            
            # Return cached result if exists
            if key in cache:
                freq_counter[key] += 1
                return cache[key]

            # Calculate new result
            result = func(*args, **kwargs)

            # If cache is full, remove least frequently used item
            if len(cache) >= maxsize:
                # Find minimum frequency
                min_freq = min(freq_counter.values())
                # Get all keys with minimum frequency
                min_freq_keys = [k for k, v in freq_counter.items() if v == min_freq]
                # Remove the oldest key with minimum frequency
                for k in insertion_order:
                    if k in min_freq_keys:
                        del cache[k]
                        del freq_counter[k]
                        insertion_order.remove(k)
                        break

            # Add new result to cache
            cache[key] = result
            freq_counter[key] = 1
            insertion_order.append(key)

            return result

        # Add clear method to wrapper
        def clear_cache():
            cache.clear()
            freq_counter.clear()
            insertion_order.clear()

        wrapper.clear_cache = clear_cache
        return wrapper

    if callable(maxsize):
        # Handle case where decorator is used without parameters
        func = maxsize
        maxsize = 128
        return decorator(func)
    return decorator
from collections import defaultdict
import functools

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Cache to store function results
        cache = {}
        # Counter to track frequency of access
        freq_counter = defaultdict(int)
        # Counter for tracking insertion order within same frequency
        insertion_counter = 0
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal insertion_counter
            
            # Create cache key based on arguments
            if typed:
                key = (args, tuple(sorted(kwargs.items())), tuple(type(arg) for arg in args))
            else:
                key = (args, tuple(sorted(kwargs.items())))
                
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
                lfu_key = min(min_freq_keys)
                cache.pop(lfu_key)
                freq_counter.pop(lfu_key)
            
            # Store new result in cache
            cache[key] = result
            freq_counter[key] = 1
            insertion_counter += 1
            
            return result
            
        # Add cache clear method
        wrapper.cache_clear = lambda: cache.clear()
        
        return wrapper
    return decorator
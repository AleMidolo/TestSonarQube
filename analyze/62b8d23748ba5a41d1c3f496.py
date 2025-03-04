from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Store cache and frequency information
        cache = {}
        freq_counter = defaultdict(int)
        freq_lists = defaultdict(set)
        min_freq = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on arguments
            key = (*args, *(kwargs.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            
            # Return cached result if exists
            if key in cache:
                # Update frequency information
                old_freq = freq_counter[key]
                freq_counter[key] += 1
                freq_lists[old_freq].remove(key)
                if not freq_lists[old_freq] and old_freq == min_freq:
                    min_freq += 1
                freq_lists[old_freq + 1].add(key)
                return cache[key]
            
            # Calculate new result
            result = func(*args, **kwargs)
            
            # If cache is full, remove least frequently used item
            if len(cache) >= maxsize:
                # Get key to remove
                lfu_key = next(iter(freq_lists[min_freq]))
                # Remove from all tracking structures
                del cache[lfu_key]
                freq_lists[min_freq].remove(lfu_key)
                del freq_counter[lfu_key]
            
            # Add new result to cache
            cache[key] = result
            freq_counter[key] = 1
            freq_lists[1].add(key)
            min_freq = 1
            
            return result
            
        # Add clear method to wrapper
        def clear():
            cache.clear()
            freq_counter.clear()
            freq_lists.clear()
            nonlocal min_freq
            min_freq = 0
            
        wrapper.clear = clear
        return wrapper
        
    return decorator
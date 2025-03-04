from collections import defaultdict
from functools import wraps

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Store cache and frequency information
        cache = {}
        freq_count = defaultdict(int)
        min_freq = 0
        freq_items = defaultdict(set)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal min_freq
            
            # Create cache key based on arguments
            if typed:
                key = (*args, *[(k, type(v), v) for k, v in kwargs.items()])
            else:
                key = (*args, *kwargs.items())
                
            # Return cached result if exists
            if key in cache:
                # Update frequency information
                old_freq = freq_count[key]
                freq_count[key] += 1
                freq_items[old_freq].remove(key)
                freq_items[freq_count[key]].add(key)
                
                # Update min frequency if needed
                if old_freq == min_freq and not freq_items[old_freq]:
                    min_freq += 1
                    
                return cache[key]
            
            # Calculate new result
            result = func(*args, **kwargs)
            
            # If cache is full, remove least frequently used item
            if len(cache) >= maxsize:
                # Get item with minimum frequency
                lfu_key = next(iter(freq_items[min_freq]))
                
                # Remove from all tracking structures
                cache.pop(lfu_key)
                freq_items[min_freq].remove(lfu_key)
                del freq_count[lfu_key]
            
            # Add new result to cache
            cache[key] = result
            freq_count[key] = 1
            freq_items[1].add(key)
            min_freq = 1
            
            return result
            
        # Add cache info method
        def cache_info():
            return {
                'hits': sum(freq_count.values()) - len(cache),
                'misses': len(cache),
                'maxsize': maxsize,
                'currsize': len(cache)
            }
            
        wrapper.cache_info = cache_info
        
        # Add cache clear method
        def cache_clear():
            cache.clear()
            freq_count.clear()
            freq_items.clear()
            nonlocal min_freq
            min_freq = 0
            
        wrapper.cache_clear = cache_clear
        
        return wrapper
    return decorator
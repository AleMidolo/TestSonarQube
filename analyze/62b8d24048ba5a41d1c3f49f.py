def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    """
    एक डेकोरेटर जो एक फ़ंक्शन को एक मेमोराइज़िंग कॉलेबल के साथ रैप करता है,
    जो `maxsize` तक के परिणामों को सेव करता है। यह एक Least Recently Used (LRU)
    एल्गोरिदम पर आधारित होता है और प्रत्येक आइटम के लिए एक समय-सीमा (Time-To-Live, TTL) 
    मान लागू करता है।
    """
    def decorator(func):
        # Create cache dict to store results and timestamps
        cache = {}
        # Create ordered dict to track LRU
        lru = collections.OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key based on args
            key = _make_key(args, kwargs, typed)
            
            curr_time = timer()
            
            # Check if result in cache and not expired
            if key in cache:
                result, timestamp = cache[key]
                if curr_time - timestamp <= ttl:
                    # Move to end of LRU
                    lru.move_to_end(key)
                    return result
                else:
                    # Remove expired item
                    del cache[key]
                    del lru[key]
            
            # Calculate new result
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = (result, curr_time)
            lru[key] = None
            
            # Remove oldest if over maxsize
            while len(cache) > maxsize:
                oldest = next(iter(lru))
                del cache[oldest]
                del lru[oldest]
                
            return result
            
        def _make_key(args, kwargs, typed):
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                if kwargs:
                    key += tuple(type(val) for val in kwargs.values())
            return hash(key)
            
        # Add cache info method
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'ttl': ttl,
            'currsize': len(cache)
        }
        
        # Add cache clear method  
        wrapper.cache_clear = lambda: cache.clear() or lru.clear()
        
        return wrapper
        
    return decorator
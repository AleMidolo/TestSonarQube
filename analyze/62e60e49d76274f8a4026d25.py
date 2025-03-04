def unit_of_work(metadata=None, timeout=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # Store the metadata and timeout settings
            wrapper.metadata = metadata
            wrapper.timeout = timeout
            return f(*args, **kwargs)
        
        # Copy function metadata
        from functools import update_wrapper
        update_wrapper(wrapper, f)
        
        # Add metadata and timeout attributes
        wrapper.metadata = metadata
        wrapper.timeout = timeout
        
        return wrapper
    return decorator
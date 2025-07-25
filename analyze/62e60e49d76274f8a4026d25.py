def unit_of_work(metadata=None, timeout=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # Store the metadata and timeout settings
            wrapper.metadata = metadata
            wrapper.timeout = timeout
            return f(*args, **kwargs)
        
        # Copy function metadata
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        
        # Add metadata and timeout as attributes
        wrapper.metadata = metadata
        wrapper.timeout = timeout
        
        return wrapper
    return decorator
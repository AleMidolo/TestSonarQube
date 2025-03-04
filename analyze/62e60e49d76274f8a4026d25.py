def unit_of_work(metadata=None, timeout=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # Store the metadata and timeout as attributes on the wrapped function
            wrapper.metadata = metadata
            wrapper.timeout = timeout
            return f(*args, **kwargs)
        
        # Copy over function metadata
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        
        return wrapper
    return decorator
def unit_of_work(metadata=None, timeout=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # Validate timeout
            if timeout is not None:
                if not isinstance(timeout, (int, float)):
                    raise TypeError("Timeout must be a number")
                if timeout < 0:
                    raise ValueError("Timeout cannot be negative")
                
            # Validate metadata
            if metadata is not None:
                if not isinstance(metadata, dict):
                    raise TypeError("Metadata must be a dictionary")
                
            # Store original function attributes
            wrapper.__name__ = f.__name__
            wrapper.__doc__ = f.__doc__
            
            # Add transaction metadata
            def wrapped_tx(tx, *args, **kwargs):
                if metadata:
                    tx.set_metadata(metadata)
                if timeout is not None:
                    tx.set_timeout(timeout)
                return f(tx, *args, **kwargs)
                
            return wrapped_tx(*args, **kwargs)
            
        return wrapper
    return decorator
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
                
            # Store transaction parameters
            tx_params = {}
            if metadata is not None:
                tx_params['metadata'] = metadata
            if timeout is not None:
                tx_params['timeout'] = timeout
                
            # Execute decorated function with transaction parameters
            def run_tx(tx):
                return f(tx, *args, **kwargs)
                
            # Return transaction function with parameters
            return run_tx
            
        return wrapper
    return decorator
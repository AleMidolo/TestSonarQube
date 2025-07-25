def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Extract the transaction object from the arguments
            tx = args[0] if args else kwargs.get('tx')
            if tx is None:
                raise ValueError("Transaction object 'tx' not found in arguments.")
            
            # Apply metadata if provided
            if metadata is not None:
                if not isinstance(metadata, dict):
                    raise TypeError("Metadata must be a dictionary.")
                tx.run("CALL dbms.setTXMetaData($metadata)", metadata=metadata)
            
            # Apply timeout if provided
            if timeout is not None:
                if not isinstance(timeout, (int, float)) or timeout < 0:
                    raise ValueError("Timeout must be a non-negative number.")
                tx.run("CALL dbms.setTransactionTimeout($timeout)", timeout=timeout * 1000)  # Convert to milliseconds
            
            # Execute the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator
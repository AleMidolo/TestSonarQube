def deprecated(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import warnings
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
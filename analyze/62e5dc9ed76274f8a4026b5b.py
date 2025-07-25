def deprecated(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import warnings
            warnings.warn(
                f"{func.__name__}: {message}",
                category=DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator
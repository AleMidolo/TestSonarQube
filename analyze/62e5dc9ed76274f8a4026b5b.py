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
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator
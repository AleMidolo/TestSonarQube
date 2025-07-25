def deprecated(message):
    """
    Decorator for deprecating functions and methods.

    ::

        @deprecated("'foo' has been deprecated in favour of 'bar'")
        def foo(x):
            pass
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Warning: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
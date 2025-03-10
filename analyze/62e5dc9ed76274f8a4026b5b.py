import functools
import warnings

def deprecated(message):
    """
    Decorador para marcar funciones y métodos como obsoletos.

    ::

        @deprecated("'foo' ha sido marcado como obsoleto en favor de 'bar'")
        def foo(x):
            pass
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated: {message}", category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
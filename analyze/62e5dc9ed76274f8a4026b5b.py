def deprecated(message):
    """
    Decorator per deprecare funzioni e metodi.
    
    Esempio di utilizzo:
    
    @deprecated("'foo' è stato deprecato a favore di 'bar'")
    def foo(x):
        pass
    """
    def decorator(func):
        import warnings
        import functools
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__}: {message}",
                category=DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
            
        return wrapper
        
    return decorator
def deprecated(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Avviso: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
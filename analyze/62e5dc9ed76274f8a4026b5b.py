def deprecated(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Warning: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
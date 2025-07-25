def deprecated(message):
    """
    返回一个用于标记函数和方法为已弃用的装饰器函数。
    用于标记函数和方法为已弃用的装饰器。
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
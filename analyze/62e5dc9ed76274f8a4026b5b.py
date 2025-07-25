import warnings
from functools import wraps

def deprecated(message):
    """
    返回一个用于标记函数和方法为已弃用的装饰器函数。
    用于标记函数和方法为已弃用的装饰器。
    @deprecated("'foo' has been deprecated in favour of 'bar'")
      def foo(x):
          pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated: {message}", DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
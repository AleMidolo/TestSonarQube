def deprecated(message):
    """
    फ़ंक्शन और विधियों को अप्रचलित घोषित करने के लिए डेकोरेटर।

    ::

        @deprecated("'foo' को 'bar' के पक्ष में अप्रचलित घोषित किया गया है")
        def foo(x):
            pass
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Warning: {func.__name__} is deprecated. {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
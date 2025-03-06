def is_fill_request_el(obj):
    """
    检查 obj 类是否具有 fill 和 request 属性。
    对象包含可执行的方法 'fill' 和 'request'。
    """
    return all(callable(getattr(obj, attr, None)) for attr in ['fill', 'request'])
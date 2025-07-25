def is_fill_request_el(obj):
    """
    检查 obj 类是否具有 fill 和 request 属性。
    对象包含可执行的方法 'fill' 和 'request'。
    """
    return hasattr(obj, 'fill') and callable(getattr(obj, 'fill')) and \
           hasattr(obj, 'request') and callable(getattr(obj, 'request'))
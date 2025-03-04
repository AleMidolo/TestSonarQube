def is_fill_compute_el(obj):
    """
    检查 obj 类是否具有 fill 和 compute 方法。
    对象包含可执行方法 'fill' 和 'compute'。
    """
    return (hasattr(obj, 'fill') and callable(getattr(obj, 'fill')) and
            hasattr(obj, 'compute') and callable(getattr(obj, 'compute')))
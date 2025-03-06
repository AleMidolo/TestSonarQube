def is_run_el(obj):
    """
    检查 obj 类是否具有 run 方法。
    对象包含可执行的方法 'run'。
    """
    return callable(getattr(obj, 'run', None))
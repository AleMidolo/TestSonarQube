def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    minimal = []
    for cls in classes:
        if not any(issubclass(other, cls) for other in classes if other is not cls):
            minimal.append(cls)
    return minimal
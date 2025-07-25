def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    minimal = []
    for cls in classes:
        is_minimal = True
        for other_cls in classes:
            if cls != other_cls and issubclass(cls, other_cls):
                is_minimal = False
                break
        if is_minimal:
            minimal.append(cls)
    return minimal
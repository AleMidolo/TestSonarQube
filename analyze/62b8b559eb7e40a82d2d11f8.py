def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    # 创建一个集合来存储所有类的子类
    subclasses = set()
    for c in classes:
        for base in classes:
            if issubclass(c, base) and c != base:
                subclasses.add(base)
    
    # 返回不在子类集合中的类的列表
    return [c for c in classes if c not in subclasses]
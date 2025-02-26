def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    # 创建一个集合来存储所有类
    all_classes = set(classes)
    # 创建一个集合来存储没有子类的类
    minimal_classes = set()

    # 遍历每个类
    for cls in classes:
        # 检查是否有子类
        has_subclass = any(cls in subclass for subclass in classes if subclass != cls)
        # 如果没有子类，则添加到最小类集合中
        if not has_subclass:
            minimal_classes.add(cls)

    # 返回有序的最小等价集合
    return sorted(minimal_classes)
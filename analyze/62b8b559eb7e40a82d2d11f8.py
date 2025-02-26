def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    # 创建一个集合来存储所有类
    all_classes = set(classes)
    # 创建一个集合来存储没有子类的类
    minimal_classes = set(all_classes)

    # 遍历所有类，检查是否有子类
    for cls in all_classes:
        for potential_subclass in all_classes:
            if cls != potential_subclass and cls in potential_subclass:
                # 如果cls是potential_subclass的父类，则从minimal_classes中移除cls
                minimal_classes.discard(cls)
                break

    # 返回没有子类的类的有序列表
    return sorted(minimal_classes)
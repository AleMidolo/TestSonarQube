def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    # 创建一个集合来存储所有类
    all_classes = set(classes)
    # 创建一个集合来存储没有子类的类
    no_subclass_classes = set(all_classes)

    # 遍历所有类，找出有子类的类
    for cls in classes:
        # 如果 cls 是其他类的子类，则从没有子类的类中移除
        for other_cls in classes:
            if cls != other_cls and issubclass(other_cls, cls):
                no_subclass_classes.discard(cls)
                break

    # 返回没有子类的类的有序列表
    return sorted(no_subclass_classes)
def minimalBases(classes):
    """
    以列表格式返回所有没有子类的类。
    将基类列表简化为其有序的最小等价集合。
    """
    # 创建一个集合来存储所有类及其子类
    all_classes = set(classes)
    subclasses = set()

    # 遍历每个类，查找其子类
    for cls in classes:
        for other_cls in classes:
            if cls != other_cls and cls in other_cls:
                subclasses.add(other_cls)

    # 找到没有子类的类
    minimal_classes = all_classes - subclasses

    # 返回有序的最小等价集合
    return sorted(minimal_classes)
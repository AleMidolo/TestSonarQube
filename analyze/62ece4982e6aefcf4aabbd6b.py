def subclasses(cls):
    """
    递归地返回一个类的所有子类。
    """
    all_subclasses = cls.__subclasses__()
    for subclass in all_subclasses:
        all_subclasses.extend(subclasses(subclass))
    return all_subclasses
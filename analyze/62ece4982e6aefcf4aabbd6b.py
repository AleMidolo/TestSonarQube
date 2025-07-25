def subclasses(cls):
    """
    递归地返回一个类的所有子类。
    """
    subclasses = cls.__subclasses__()
    for subclass in subclasses:
        subclasses += subclasses(subclass)
    return subclasses
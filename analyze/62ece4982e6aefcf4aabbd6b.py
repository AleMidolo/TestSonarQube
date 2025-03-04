def subclasses(cls):
    """
    递归地返回一个类的所有子类。
    """
    subs = cls.__subclasses__()
    result = []
    for sub in subs:
        result.append(sub)
        result.extend(subclasses(sub))
    return result
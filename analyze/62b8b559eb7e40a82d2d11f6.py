def determineMetaclass(bases, explicit_mc=None):
    """
    从一个或多个基类以及可选的显式 __metaclass__ 中确定元类。
    """
    if explicit_mc is not None:
        return explicit_mc

    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type

    # 取所有元类的交集
    metaclass = metaclasses[0]
    for m in metaclasses[1:]:
        if not issubclass(m, metaclass):
            metaclass = type('CombinedMeta', (metaclass, m), {})
    
    return metaclass
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
    for mc in metaclasses[1:]:
        if not issubclass(mc, metaclass):
            raise TypeError("基类的元类不一致")
        metaclass = mc

    return metaclass
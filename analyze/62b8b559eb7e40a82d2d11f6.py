def determineMetaclass(bases, explicit_mc=None):
    """
    从一个或多个基类以及可选的显式 __metaclass__ 中确定元类。
    """
    if explicit_mc is not None:
        metaclass = explicit_mc
    elif bases:
        metaclass = type(bases[0])
        for base in bases[1:]:
            if type(base) is not metaclass:
                metaclass = type
                break
    else:
        metaclass = type
    return metaclass
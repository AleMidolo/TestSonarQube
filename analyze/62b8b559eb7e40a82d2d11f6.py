def determineMetaclass(bases, explicit_mc=None):
    """
    从一个或多个基类以及可选的显式 __metaclass__ 中确定元类。
    """
    if explicit_mc is not None:
        return explicit_mc
    metaclass = type(bases[0]) if bases else type
    for base in bases[1:]:
        base_metaclass = type(base)
        if base_metaclass is not metaclass:
            if metaclass is not type:
                if base_metaclass is not type:
                    raise TypeError("metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases")
            else:
                metaclass = base_metaclass
    return metaclass
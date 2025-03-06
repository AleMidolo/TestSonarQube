def determineMetaclass(bases, explicit_mc=None):
    """
    从一个或多个基类以及可选的显式 __metaclass__ 中确定元类。
    """
    if explicit_mc is not None:
        return explicit_mc
    for base in bases:
        if hasattr(base, '__class__'):
            return base.__class__
    return type
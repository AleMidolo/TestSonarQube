def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__.
    
    Args:
        bases: A tuple of base classes.
        explicit_mc: An optional explicit metaclass.
    
    Returns:
        The determined metaclass.
    """
    if explicit_mc is not None:
        return explicit_mc
    
    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type
    
    # Find the most derived metaclass
    candidate = metaclasses[0]
    for mc in metaclasses[1:]:
        if not issubclass(candidate, mc):
            if issubclass(mc, candidate):
                candidate = mc
            else:
                raise TypeError("metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases")
    
    return candidate
def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__.
    
    Args:
        bases (tuple): A tuple of base classes.
        explicit_mc (type, optional): An explicitly provided metaclass.
    
    Returns:
        type: The determined metaclass.
    """
    if explicit_mc is not None:
        return explicit_mc
    
    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type
    
    # Find the most derived metaclass
    candidate = metaclasses[0]
    for mc in metaclasses[1:]:
        if issubclass(mc, candidate):
            candidate = mc
        elif not issubclass(candidate, mc):
            # If neither is a subclass of the other, raise TypeError
            raise TypeError("metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases")
    
    return candidate
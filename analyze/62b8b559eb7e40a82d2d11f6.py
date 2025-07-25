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
    
    metaclass = type(bases[0])
    for base in bases[1:]:
        if type(base) is not metaclass:
            return type
    
    return metaclass
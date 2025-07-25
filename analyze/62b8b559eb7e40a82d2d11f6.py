def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    # Start with explicit metaclass if provided
    metaclass = explicit_mc
    
    # If no explicit metaclass, get metaclass from first base
    if metaclass is None and bases:
        metaclass = type(bases[0])
        
    # Check remaining bases for metaclass conflicts
    for base in bases[1:]:
        base_mc = type(base)
        if issubclass(metaclass, base_mc):
            continue
        if issubclass(base_mc, metaclass):
            metaclass = base_mc
            continue
        # Incompatible metaclasses
        raise TypeError("Incompatible metaclasses: %s and %s" % 
                       (metaclass.__name__, base_mc.__name__))
                       
    return metaclass if metaclass is not None else type
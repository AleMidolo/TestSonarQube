def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclase a partir de una o más clases base y un __metaclase__ explícito opcional.
    """
    if explicit_mc is not None:
        return explicit_mc
    
    metaclass_candidates = [type(base) for base in bases]
    
    if not metaclass_candidates:
        return type
    
    metaclass = metaclass_candidates[0]
    for candidate in metaclass_candidates[1:]:
        if candidate is not metaclass:
            raise TypeError("metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases")
    
    return metaclass
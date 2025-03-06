def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclase a partir de una o más clases base y un __metaclass__ explícito opcional.
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
            else:
                metaclass = base_metaclass
    
    return metaclass
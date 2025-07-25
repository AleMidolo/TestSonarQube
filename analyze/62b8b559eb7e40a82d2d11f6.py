def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclase a partir de una o más clases base y un __metaclass__ explícito opcional.
    """
    if explicit_mc is not None:
        metaclass = explicit_mc
    else:
        metaclass = type(bases[0]) if bases else type
    
    for base in bases[1:]:
        base_metaclass = type(base)
        if base_metaclass is not metaclass:
            metaclass = type
    
    return metaclass
def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclase a partir de una o más clases base y un __metaclass__ explícito opcional.
    """
    if explicit_mc is not None:
        return explicit_mc
    
    metaclass = type(bases[0])
    for base in bases[1:]:
        if type(base) is not metaclass:
            return type
    
    return metaclass
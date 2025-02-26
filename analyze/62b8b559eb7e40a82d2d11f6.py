def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclasse a partire da una o più basi e da un'eventuale __metaclass__ esplicita.
    """
    if explicit_mc is not None:
        return explicit_mc

    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type

    # Find the common metaclass
    common_metaclass = metaclasses[0]
    for mc in metaclasses[1:]:
        if not issubclass(mc, common_metaclass):
            common_metaclass = type('Meta', (common_metaclass, mc), {})
    
    return common_metaclass
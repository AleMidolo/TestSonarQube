def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclasse a partire da una o più basi e da un'eventuale __metaclass__ esplicita.
    """
    if explicit_mc is not None:
        return explicit_mc
    for base in bases:
        if hasattr(base, '__class__'):
            return base.__class__
    return type
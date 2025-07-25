def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclasse a partire da una o più basi e da un'eventuale __metaclass__ esplicita.
    """
    # If there's an explicit metaclass, start with that
    metaclass = explicit_mc
    
    # If no explicit metaclass, look through the bases
    if metaclass is None:
        if bases:
            # Get metaclasses from all base classes
            metaclasses = [type(base) for base in bases]
            # Find most derived metaclass
            metaclass = metaclasses[0]
            for mc in metaclasses[1:]:
                if issubclass(mc, metaclass):
                    metaclass = mc
                elif not issubclass(metaclass, mc):
                    raise TypeError("Incompatible metaclasses")
        else:
            # No bases and no explicit metaclass, use type
            metaclass = type
            
    # If we have an explicit metaclass, ensure it's compatible with base metaclasses
    elif bases:
        # Check that explicit metaclass is compatible with all base metaclasses
        for base in bases:
            if not issubclass(metaclass, type(base)):
                raise TypeError("Explicit metaclass not compatible with base metaclasses")
                
    return metaclass
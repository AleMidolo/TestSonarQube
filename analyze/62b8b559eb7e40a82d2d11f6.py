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
            # Find the most derived metaclass
            metaclass = metaclasses[0]
            for mc in metaclasses[1:]:
                if issubclass(mc, metaclass):
                    metaclass = mc
                elif not issubclass(metaclass, mc):
                    # If metaclasses are not compatible, raise error
                    raise TypeError("Incompatible metaclasses found")
        else:
            # If no bases, use type as default metaclass
            metaclass = type
            
    # If explicit metaclass was provided, ensure it's compatible with base metaclasses
    else:
        for base in bases:
            if not issubclass(metaclass, type(base)):
                raise TypeError(f"Explicit metaclass {metaclass} is not compatible with base class metaclass {type(base)}")
    
    return metaclass
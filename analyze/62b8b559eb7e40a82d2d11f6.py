def determineMetaclass(bases, explicit_mc=None):
    """
    1 या अधिक बेस क्लास और वैकल्पिक स्पष्ट __metaclass__ से मेटाक्लास निर्धारित करें।
    """
    metaclass = None
    
    # Check explicit metaclass first if provided
    if explicit_mc is not None:
        metaclass = explicit_mc
        
    # Look for metaclass in base classes
    for base in bases:
        base_mc = type(base)
        
        if metaclass is None:
            metaclass = base_mc
        elif issubclass(base_mc, metaclass):
            # If base metaclass is more specific, use it
            metaclass = base_mc
        elif issubclass(metaclass, base_mc):
            # Current metaclass is more specific, keep it
            continue
        else:
            # Incompatible metaclasses
            raise TypeError("Incompatible metaclasses found")
            
    # If no metaclass found, use type
    if metaclass is None:
        metaclass = type
        
    return metaclass
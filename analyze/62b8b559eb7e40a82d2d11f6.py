def determineMetaclass(bases, explicit_mc=None):
    """
    1 या अधिक बेस क्लास और वैकल्पिक स्पष्ट __metaclass__ से मेटाक्लास निर्धारित करें।
    """
    if explicit_mc is not None:
        return explicit_mc
    
    metaclass = type(bases[0])
    for base in bases[1:]:
        if type(base) is not metaclass:
            raise TypeError("Metaclass conflict: the bases have different metaclasses")
    
    return metaclass
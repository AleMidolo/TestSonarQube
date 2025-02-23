def determineMetaclass(bases, explicit_mc=None):
    """
    1 या अधिक बेस क्लास और वैकल्पिक स्पष्ट __metaclass__ से मेटाक्लास निर्धारित करें।
    """
    if explicit_mc is not None:
        return explicit_mc

    metaclasses = [type(base) for base in bases]
    if not metaclasses:
        return type

    metaclass = metaclasses[0]
    for mc in metaclasses[1:]:
        if not issubclass(mc, metaclass):
            raise TypeError("Inconsistent metaclass for bases: {}".format(bases))
    
    return metaclass
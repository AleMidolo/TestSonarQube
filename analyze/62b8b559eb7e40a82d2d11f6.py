def determineMetaclass(bases, explicit_mc=None):
    """
    1 या अधिक बेस क्लास और वैकल्पिक स्पष्ट __metaclass__ से मेटाक्लास निर्धारित करें।
    """
    if explicit_mc is not None:
        return explicit_mc
    for base in bases:
        if hasattr(base, '__class__'):
            return base.__class__
    return type
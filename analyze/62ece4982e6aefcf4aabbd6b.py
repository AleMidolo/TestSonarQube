def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    subs = cls.__subclasses__()
    for sub in cls.__subclasses__():
        subs.extend(subclasses(sub))
    return subs
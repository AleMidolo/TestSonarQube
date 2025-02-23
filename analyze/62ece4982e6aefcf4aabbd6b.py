def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    return cls.__subclasses__() + [sub for c in cls.__subclasses__() for sub in subclasses(c)]
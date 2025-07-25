def subclasses(cls):
    """
    Return all subclasses of a class, recursively.
    """
    subclasses = cls.__subclasses__()
    for subclass in subclasses:
        subclasses += subclasses(subclass)
    return subclasses
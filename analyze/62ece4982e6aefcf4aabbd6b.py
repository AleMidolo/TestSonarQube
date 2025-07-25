def subclasses(cls):
    """
    Restituisce tutte le sottoclassi di una classe, ricorsivamente.
    """
    subclasses = cls.__subclasses__()
    for subclass in subclasses:
        subclasses += subclasses(subclass)
    return subclasses
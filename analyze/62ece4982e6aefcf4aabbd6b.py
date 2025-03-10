def subclasses(cls):
    """
    Devuelve todas las subclases de una clase, de forma recursiva.
    """
    subclasses = cls.__subclasses__()
    for subclass in subclasses:
        subclasses += subclasses(subclass)
    return subclasses
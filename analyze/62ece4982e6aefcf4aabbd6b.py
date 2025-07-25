def subclasses(cls):
    """
    Devuelve todas las subclases de una clase, de forma recursiva.
    """
    subcls = cls.__subclasses__()
    for subclass in subcls:
        subcls.extend(subclasses(subclass))
    return subcls
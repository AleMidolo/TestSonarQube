def subclasses(cls):
    """
    Restituisce tutte le sottoclassi di una classe, ricorsivamente.
    """
    result = set()
    for subclass in cls.__subclasses__():
        result.add(subclass)
        result.update(subclasses(subclass))
    return result
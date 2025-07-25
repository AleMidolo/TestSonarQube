def subclasses(cls):
    """
    Restituisce tutte le sottoclassi di una classe, ricorsivamente.
    """
    def _subclasses(cls):
        for subclass in cls.__subclasses__():
            yield subclass
            yield from _subclasses(subclass)
    
    return list(_subclasses(cls))
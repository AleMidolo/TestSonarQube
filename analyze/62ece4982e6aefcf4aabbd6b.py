def subclasses(cls):
    """
    Restituisce tutte le sottoclassi di una classe, ricorsivamente.
    """
    subclasses_list = cls.__subclasses__()
    for subclass in cls.__subclasses__():
        subclasses_list.extend(subclasses(subclass))
    return subclasses_list
def subclasses(cls):
    """
    Restituisce tutte le sottoclassi di una classe, ricorsivamente.
    """
    subclasses_list = cls.__subclasses__()
    for subclass in subclasses_list:
        subclasses_list.extend(subclasses(subclass))
    return subclasses_list
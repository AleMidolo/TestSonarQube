def subclasses(cls):
    """
    Devuelve todas las subclases de una clase, de forma recursiva.
    """
    subclasses_list = cls.__subclasses__()
    for subclass in subclasses_list:
        subclasses_list.extend(subclasses(subclass))
    return subclasses_list
def subclasses(cls):
    """
    Devuelve todas las subclases de una clase, de forma recursiva.
    """
    subs = cls.__subclasses__()
    result = []
    for sub in subs:
        result.append(sub)
        result.extend(subclasses(sub))
    return result
def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    all_subclasses = cls.__subclasses__()
    for subclass in all_subclasses:
        all_subclasses.extend(subclasses(subclass))
    return all_subclasses
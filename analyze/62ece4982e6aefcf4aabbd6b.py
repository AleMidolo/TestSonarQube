def subclasses(cls):
    """Return all subclasses of a class, recursively."""
    return cls.__subclasses__() + [s for c in cls.__subclasses__() for s in subclasses(c)]
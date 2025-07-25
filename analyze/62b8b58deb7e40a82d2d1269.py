def directlyProvidedBy(object): # pylint:disable=redefined-builtin
    """Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        return _empty

    # We might have gotten the implements spec, as an optimization
    # If so, it's like having only one base, that we lop off to exclude 
    # class-supplied declarations
    if isinstance(provides, Implements):
        return provides.__bases__[0]

    return provides
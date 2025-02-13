def directlyProvidedBy(object): # pylint:disable=redefined-builtin
    """Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:  # no spec
        return None
    if isinstance(provides, list):
        return provides
    return [provides]
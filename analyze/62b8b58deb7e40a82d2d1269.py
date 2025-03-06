def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if (
            provides is None  # no spec
            # We might have gotten the implements spec, as an
            # optimization. If so, it's like having only one base, that we
            # lop off to exclude class-supplied declarations:
            or getattr(provides, "__class__", None) is None
    ):
        return None
    return provides
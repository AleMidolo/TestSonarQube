def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    proporciona = getattr(object, "__provides__", None)
    if proporciona is None:
        return None
    return proporciona
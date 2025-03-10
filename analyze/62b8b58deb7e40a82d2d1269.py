def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    proporciona = getattr(object, "__provides__", None)
    if (
            proporciona is None  # sin especificación
            # Podríamos haber obtenido la especificación de implementación, como una
            # optimización. Si es así, es como tener solo una base, que
            # eliminamos para excluir declaraciones proporcionadas por la clase:
    ):
        return None
    return proporciona
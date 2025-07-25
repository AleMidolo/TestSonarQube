def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    proporciona = getattr(object, "__provides__", None)
    if proporciona is None:
        return None  # Sin especificación

    # Aquí podríamos agregar lógica adicional para manejar la optimización
    # y excluir declaraciones proporcionadas por la clase base.

    return proporciona
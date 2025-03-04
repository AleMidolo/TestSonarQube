def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        return _empty
        
    # Podríamos haber obtenido la especificación de implementación como una optimización
    # Si es así, es como tener solo una base que eliminamos para excluir 
    # declaraciones proporcionadas por la clase
    spec = provides
    bases = spec.__bases__
    if len(bases) == 1 and bases[0] is getattr(object, "__implemented__", None):
        return _empty
        
    return provides
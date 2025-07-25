def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    
    if provides is None:
        return _empty
        
    # Si provides es una especificación de implementación, necesitamos excluir
    # las declaraciones proporcionadas por la clase
    spec = provides
    if spec.isImplementation():
        spec = spec.__without_bases__()
        
    return spec
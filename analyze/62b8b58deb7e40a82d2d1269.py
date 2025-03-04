def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    
    if provides is None:
        # No hay especificación directa
        return _empty
        
    # Si provides es una especificación de implementación (optimización),
    # la tratamos como si tuviera una sola base que eliminamos
    # para excluir declaraciones proporcionadas por la clase
    if hasattr(provides, 'inherit'):
        provides = provides.__bases__[0]
        
    return provides
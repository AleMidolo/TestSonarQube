def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """
    Devuelve las interfaces proporcionadas directamente por el objeto dado.

    El valor devuelto es un `~zope.interface.interfaces.IDeclaration`.
    """
    from zope.interface.declarations import Provides
    from zope.interface.interface import InterfaceClass
    
    provides = getattr(object, "__provides__", None)
    
    if provides is None:
        return Provides(InterfaceClass("empty"))
        
    # Si provides es una implementación de clase, retornar una declaración vacía
    if len(provides.__bases__) == 1:
        return Provides(InterfaceClass("empty")) 
        
    # Retornar las interfaces directamente proporcionadas
    return provides
def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Restituisce le interfacce direttamente fornite dall'oggetto dato.

    Il valore restituito è un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        return _empty
        
    # Se provides è un'implementazione di classe, restituisci vuoto
    if isinstance(provides, Implements):
        return _empty
        
    # Altrimenti restituisci le interfacce direttamente fornite
    return provides
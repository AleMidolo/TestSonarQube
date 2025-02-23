def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Restituisce le interfacce direttamente fornite dall'oggetto dato.

    Il valore restituito è un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:  # nessuna specifica
        return None  # Nessuna interfaccia fornita

    # Se abbiamo una specifica "implements", la consideriamo
    if isinstance(provides, list):
        return provides  # Restituiamo la lista delle interfacce fornite

    return [provides]  # Restituiamo un elenco con un'unica interfaccia fornita
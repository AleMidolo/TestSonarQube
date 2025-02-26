def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Restituisce le interfacce direttamente fornite dall'oggetto dato.

    Il valore restituito è un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:  # nessuna specifica
        return None  # Nessuna interfaccia fornita

    # Se abbiamo una specifica "implements", trattiamola come una sola base
    if isinstance(provides, list) and len(provides) == 1:
        return provides[0]

    return provides
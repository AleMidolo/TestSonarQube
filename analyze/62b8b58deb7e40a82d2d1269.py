def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Restituisce le interfacce direttamente fornite dall'oggetto dato.

    Il valore restituito è un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:  # nessuna specifica
        return None  # Nessuna interfaccia fornita

    # Se abbiamo una specifica "implements", la escludiamo
    if hasattr(object, "__implements__"):
        return None  # Escludiamo dichiarazioni fornite dalla classe

    return provides  # Restituisce le interfacce fornite
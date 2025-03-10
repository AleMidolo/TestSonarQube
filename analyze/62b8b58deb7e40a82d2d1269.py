def directlyProvidedBy(object):  # pylint:disable=redefined-builtin
    """Restituisce le interfacce direttamente fornite dall'oggetto dato.

    Il valore restituito è un `~zope.interface.interfaces.IDeclaration`.
    """
    provides = getattr(object, "__provides__", None)
    if (
            provides is None  # nessuna specifica
            # Potremmo aver ottenuto la specifica "implements", come
            # ottimizzazione. In tal caso, è come avere una sola base, che
            # escludiamo per evitare dichiarazioni fornite dalla classe:
            or getattr(provides, "__bases__", ()) == (object,)
    ):
        return None
    return provides
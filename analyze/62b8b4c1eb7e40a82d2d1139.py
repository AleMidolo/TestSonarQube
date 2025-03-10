def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    
    :param iface: L'interfaccia da verificare.
    :param candidate: La classe o oggetto da verificare.
    :param tentative: Se True, restituisce un valore booleano invece di sollevare un'eccezione.
    :return: True se il candidato soddisfa l'interfaccia, altrimenti False se tentative è True.
    :raises: TypeError se il candidato non soddisfa l'interfaccia e tentative è False.
    """
    if not all(hasattr(candidate, attr) for attr in dir(iface) if not attr.startswith('__')):
        if tentative:
            return False
        else:
            raise TypeError(f"{candidate.__name__} does not implement all required methods of {iface.__name__}")
    return True
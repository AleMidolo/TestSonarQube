def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    
    :param iface: L'interfaccia da verificare.
    :param candidate: La classe o oggetto candidato da verificare.
    :param tentative: Se True, verifica solo i metodi senza sollevare eccezioni.
    :return: True se il candidato soddisfa l'interfaccia, altrimenti False.
    """
    if not hasattr(iface, '__abstractmethods__'):
        raise TypeError(f"{iface} non è un'interfaccia valida.")
    
    abstract_methods = iface.__abstractmethods__
    
    for method in abstract_methods:
        if not hasattr(candidate, method):
            if tentative:
                return False
            else:
                raise TypeError(f"Il candidato non implementa il metodo richiesto: {method}")
    
    return True
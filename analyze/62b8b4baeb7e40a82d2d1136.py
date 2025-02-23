def _verify(iface, candidate, tentative=False, vtype=None):
    """
    Verifica che il *candidate* possa fornire correttamente l'*iface*.

    Questo processo include:

    - Assicurarsi che il candidato dichiari di fornire l'interfaccia utilizzando ``iface.providedBy`` (a meno che *tentative* sia `True`, in quel caso questo passaggio viene saltato). Questo significa che la classe del candidato dichiara di `implementare l'interfaccia <zope.interface.implementer>`, oppure che il candidato stesso dichiara di `fornire l'interfaccia <zope.interface.provider>`.

    - Assicurarsi che il candidato definisca tutti i metodi necessari.

    - Assicurarsi che i metodi abbiano la firma corretta (per quanto possibile).

    - Assicurarsi che il candidato definisca tutti gli attributi necessari.

    :return bool: Restituisce un valore vero se tutto ciò che poteva essere verificato è stato superato.
    :raises zope.interface.Invalid: Se una qualsiasi delle condizioni precedenti non è soddisfatta.

    .. versionchanged:: 5.0  
        Se più metodi o attributi sono invalidi, tutti questi errori vengono raccolti e riportati. In precedenza, veniva segnalato solo il primo errore. Come caso speciale, se è presente un solo errore, questo viene sollevato singolarmente, come avveniva prima.
    """
    from zope.interface import providedBy, Invalid
    from inspect import signature

    errors = []

    if not tentative and not providedBy(candidate).isOrExtends(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.__providedBy__.methods()
    for method in required_methods:
        if not hasattr(candidate, method):
            errors.append(f"{candidate} is missing method {method}")
            continue
        
        # Check method signature
        candidate_method = getattr(candidate, method)
        if not callable(candidate_method):
            errors.append(f"{method} in {candidate} is not callable")
            continue
        
        iface_signature = signature(getattr(iface, method))
        candidate_signature = signature(candidate_method)
        
        if len(candidate_signature.parameters) < len(iface_signature.parameters):
            errors.append(f"{method} in {candidate} has incorrect signature")

    required_attributes = iface.__providedBy__.attributes()
    for attr in required_attributes:
        if not hasattr(candidate, attr):
            errors.append(f"{candidate} is missing attribute {attr}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)

    return True
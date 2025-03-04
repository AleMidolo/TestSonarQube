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
    from inspect import signature, isfunction

    errors = []

    if not tentative and not providedBy(candidate).provides(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.names()
    for method_name in required_methods:
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue
        
        method = getattr(candidate, method_name)
        if not isfunction(method):
            errors.append(f"{method_name} in {candidate} is not a function")
            continue
        
        # Check method signature
        expected_signature = signature(iface[method_name])
        actual_signature = signature(method)
        if len(expected_signature.parameters) != len(actual_signature.parameters):
            errors.append(f"{method_name} in {candidate} has incorrect number of parameters")
    
    required_attributes = iface.attributes()
    for attr_name in required_attributes:
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)

    return True
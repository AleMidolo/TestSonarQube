def verifyObject(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente la interfaz *iface*.

    Esto implica:

    - Asegurarse de que el candidato afirma que proporciona la interfaz utilizando ``iface.providedBy`` (a menos que *tentative* sea `True`, en cuyo caso este paso se omite). Esto significa que la clase del candidato declara que `implementa <zope.interface.implementer>` la interfaz, o que el propio candidato declara que `proporciona <zope.interface.provider>` la interfaz.

    - Asegurarse de que el candidato define todos los métodos necesarios.

    - Asegurarse de que los métodos tienen la firma correcta (en la medida de lo posible).

    - Asegurarse de que el candidato define todos los atributos necesarios.

    :return bool: Devuelve un valor verdadero si todo lo que se pudo verificar pasó correctamente.
    :raises zope.interface.Invalid: Si alguna de las condiciones anteriores no se cumple.

    .. versionchanged:: 5.0  
        Si múltiples métodos o atributos son inválidos, todos esos errores se recopilan y se informan. Anteriormente, solo se informaba el primer error. Como caso especial, si solo hay un error presente, este se lanza de forma individual, como antes.
    """
    from zope.interface import providedBy, Invalid
    from inspect import signature, isfunction
    import inspect

    errors = []

    if not tentative and not providedBy(candidate).isOrExtends(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.names().keys()
    for method_name in required_methods:
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue
        
        method = getattr(candidate, method_name)
        if not isfunction(method):
            errors.append(f"{method_name} in {candidate} is not a function")
            continue
        
        iface_method = iface.lookupMethod(method_name)
        if iface_method is not None:
            iface_signature = signature(iface_method)
            method_signature = signature(method)
            if iface_signature != method_signature:
                errors.append(f"Signature mismatch for {method_name} in {candidate}")

    required_attributes = [attr for attr in iface.names() if not callable(getattr(iface, attr))]
    for attr in required_attributes:
        if not hasattr(candidate, attr):
            errors.append(f"{candidate} is missing attribute {attr}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid(errors)

    return True
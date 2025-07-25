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
    from inspect import signature, Parameter

    errors = []

    if not tentative and not providedBy(candidate).isOrExtends(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.names()
    for method_name, _ in required_methods:
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue
        
        method = getattr(candidate, method_name)
        iface_method = iface.lookupMethod(method_name)
        
        if not callable(method):
            errors.append(f"{method_name} in {candidate} is not callable")
            continue
        
        if signature(method) != signature(iface_method):
            errors.append(f"{method_name} in {candidate} has incorrect signature")

    required_attributes = iface.names()
    for attr_name, _ in required_attributes:
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid(errors)

    return True
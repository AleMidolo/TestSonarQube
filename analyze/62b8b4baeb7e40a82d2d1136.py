def _verify(iface, candidate, tentative=False, vtype=None):
    """
    Verifica que *candidate* pueda proporcionar correctamente *iface*.

    Esto implica:

    - Asegurarse de que el candidato afirme que proporciona la
      interfaz utilizando ``iface.providedBy`` (a menos que *tentative* sea `True`,
      en cuyo caso este paso se omite). Esto significa que la clase del candidato
      declara que `implementa <zope.interface.implementer>` la interfaz,
      o que el propio candidato declara que `proporciona <zope.interface.provider>`
      la interfaz.

    - Asegurarse de que el candidato defina todos los métodos necesarios.

    - Asegurarse de que los métodos tengan la firma correcta (en la
      medida de lo posible).

    - Asegurarse de que el candidato defina todos los atributos necesarios.

    :return bool: Devuelve un valor verdadero si todo lo que se pudo
       verificar pasó.
    :raises zope.interface.Invalid: Si alguna de las condiciones anteriores
       no se cumple.

    .. versionchanged:: 5.0
        Si múltiples métodos o atributos son inválidos, todos esos errores
        se recopilan y se informan. Anteriormente, solo se informaba el primer error.
        Como caso especial, si solo hay un error presente, se lanza
        de forma individual, como antes.
    """
    from zope.interface import providedBy, Invalid
    from inspect import signature, isfunction

    errors = []

    if not tentative and not providedBy(candidate)(iface):
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
        expected_signature = signature(getattr(iface, method_name))
        actual_signature = signature(method)
        if expected_signature != actual_signature:
            errors.append(f"Signature mismatch for {method_name} in {candidate}")

    required_attributes = iface.attributes()
    for attr_name in required_attributes:
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid(errors)

    return True
from zope.interface import Invalid, providedBy
import inspect

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
    errors = []

    # Verificar si el candidato proporciona la interfaz, a menos que tentative sea True
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"El candidato no proporciona la interfaz {iface.__name__}.")

    # Verificar métodos requeridos
    for method_name in iface.names():
        if not hasattr(candidate, method_name):
            errors.append(f"El candidato no tiene el método requerido: {method_name}.")
            continue

        # Verificar la firma del método si es posible
        candidate_method = getattr(candidate, method_name)
        if inspect.isfunction(candidate_method) or inspect.ismethod(candidate_method):
            try:
                inspect.signature(candidate_method)
            except ValueError:
                errors.append(f"La firma del método {method_name} no es válida.")

    # Verificar atributos requeridos
    for attr_name in iface.names(all=True):
        if not hasattr(candidate, attr_name):
            errors.append(f"El candidato no tiene el atributo requerido: {attr_name}.")

    # Manejar errores
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
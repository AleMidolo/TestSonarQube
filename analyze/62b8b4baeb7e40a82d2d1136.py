from zope.interface import Invalid, providedBy
from inspect import signature

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
    errors = []

    # Verificar si el candidato proporciona la interfaz
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"{candidate} no proporciona la interfaz {iface}")

    # Verificar métodos requeridos
    required_methods = iface.namesAndDescriptions(all=True)
    for name, desc in required_methods:
        if not hasattr(candidate, name):
            errors.append(f"El método requerido '{name}' no está definido en {candidate}")
        else:
            # Verificar la firma del método
            candidate_method = getattr(candidate, name)
            if callable(candidate_method):
                try:
                    sig = signature(candidate_method)
                    expected_sig = signature(desc.getSignature())
                    if sig != expected_sig:
                        errors.append(f"La firma del método '{name}' no coincide: esperado {expected_sig}, obtenido {sig}")
                except ValueError:
                    # Si no se puede obtener la firma, se omite la verificación
                    pass

    # Verificar atributos requeridos
    required_attrs = iface.namesAndDescriptions(all=True)
    for name, desc in required_attrs:
        if not hasattr(candidate, name):
            errors.append(f"El atributo requerido '{name}' no está definido en {candidate}")

    # Manejar errores
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
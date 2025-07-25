from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject as zope_verifyObject

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
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"The candidate does not provide the interface {iface}.")

    try:
        zope_verifyObject(iface, candidate)
    except Invalid as e:
        raise Invalid(f"Verification failed: {e}")

    return True
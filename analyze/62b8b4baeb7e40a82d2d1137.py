from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject as zope_verifyObject

def verifyObject(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente l'*iface*.

    Questo comporta:

    - Assicurarsi che il candidato dichiari di fornire l'interfaccia utilizzando ``iface.providedBy`` (a meno che *tentative* sia `True`, nel qual caso questo passaggio viene saltato). Questo significa che la classe del candidato dichiara di `implementare <zope.interface.implementer>` l'interfaccia, oppure che il candidato stesso dichiara di `fornire <zope.interface.provider>` l'interfaccia.

    - Assicurarsi che il candidato definisca tutti i metodi necessari.

    - Assicurarsi che i metodi abbiano la firma corretta (per quanto possibile).

    - Assicurarsi che il candidato definisca tutti gli attributi necessari.

    :return bool: Restituisce un valore vero se tutto ciò che poteva essere verificato è stato superato.
    :raises zope.interface.Invalid: Se una qualsiasi delle condizioni precedenti non è soddisfatta.

    .. versionchanged:: 5.0  
        Se più metodi o attributi sono invalidi, tutti questi errori vengono raccolti e riportati. In precedenza, veniva segnalato solo il primo errore. Come caso speciale, se è presente un solo errore, viene sollevato singolarmente, come in passato.
    """
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"The candidate does not provide the interface {iface}.")

    try:
        zope_verifyObject(iface, candidate)
    except Invalid as e:
        raise Invalid(f"Verification failed: {e}")

    return True
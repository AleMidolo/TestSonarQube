from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject, verifyClass

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
    errors = []

    # Verifica che il candidato fornisca l'interfaccia, a meno che non sia tentative
    if not tentative:
        if not providedBy(candidate, iface):
            errors.append(f"{candidate} non fornisce l'interfaccia {iface}")

    # Verifica i metodi e gli attributi
    try:
        if vtype == 'class':
            verifyClass(iface, candidate)
        else:
            verifyObject(iface, candidate)
    except Invalid as e:
        errors.append(str(e))

    # Se ci sono errori, solleva un'eccezione Invalid con tutti gli errori
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
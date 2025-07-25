from zope.interface import providedBy, verify
from zope.interface.exceptions import Invalid
from zope.interface.interface import Method, Attribute

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
    errors = []

    # Verifica che il candidato dichiari di fornire l'interfaccia
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"{candidate} non dichiara di fornire l'interfaccia {iface}")

    # Verifica i metodi e gli attributi
    for name in iface.names(all=True):
        if name not in dir(candidate):
            errors.append(f"{candidate} non definisce l'attributo/metodo {name}")
            continue

        # Verifica la firma dei metodi
        if isinstance(iface[name], Method):
            candidate_method = getattr(candidate, name)
            if not callable(candidate_method):
                errors.append(f"{name} non è un metodo in {candidate}")
            else:
                # Verifica la firma del metodo (semplificata)
                iface_method = iface[name]
                candidate_sig = getattr(candidate_method, '__annotations__', {})
                iface_sig = getattr(iface_method, '__annotations__', {})
                if candidate_sig != iface_sig:
                    errors.append(f"La firma di {name} non corrisponde in {candidate}")

    # Gestione degli errori
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
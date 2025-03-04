def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.interface import Method
    from collections import defaultdict

    if not tentative and not iface.providedBy(candidate):
        raise DoesNotImplement(iface)

    errors = defaultdict(list)

    # Verifica metodi
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Verifica che il metodo esista
            try:
                attr = getattr(candidate, name)
            except AttributeError:
                errors['missing_methods'].append(name)
                continue

            # Verifica che sia chiamabile
            if not callable(attr):
                errors['not_callable'].append(name)
                continue

            # Verifica la firma del metodo
            try:
                desc.validateSignature(attr)
            except Invalid as e:
                errors['invalid_signature'].append((name, str(e)))

    # Verifica attributi
    for name, desc in iface.namesAndDescriptions(0):
        if not isinstance(desc, Method):
            try:
                getattr(candidate, name)
            except AttributeError:
                errors['missing_attributes'].append(name)

    # Gestione errori
    if not errors:
        return True

    # Crea messaggi di errore
    error_messages = []
    if errors['missing_methods']:
        error_messages.append(f"Metodi mancanti: {', '.join(errors['missing_methods'])}")
    if errors['not_callable']:
        error_messages.append(f"Attributi non chiamabili: {', '.join(errors['not_callable'])}")
    if errors['invalid_signature']:
        sig_errors = [f"{name}: {err}" for name, err in errors['invalid_signature']]
        error_messages.append(f"Firme non valide: {', '.join(sig_errors)}")
    if errors['missing_attributes']:
        error_messages.append(f"Attributi mancanti: {', '.join(errors['missing_attributes'])}")

    # Se c'è un solo tipo di errore, solleva l'eccezione appropriata
    if len(error_messages) == 1:
        if errors['missing_methods'] or errors['missing_attributes']:
            raise BrokenImplementation(iface, error_messages[0])
        if errors['not_callable'] or errors['invalid_signature']:
            raise BrokenMethodImplementation(iface, error_messages[0])

    # Altrimenti, solleva un'eccezione con tutti gli errori
    raise Invalid("\n".join(error_messages))
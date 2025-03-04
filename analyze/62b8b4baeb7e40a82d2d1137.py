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
                from inspect import signature
                impl_sig = signature(attr)
                desc_sig = signature(desc)
                
                if impl_sig != desc_sig:
                    errors['wrong_signature'].append((name, str(desc_sig), str(impl_sig)))
            except ValueError:
                # Non è possibile ottenere la firma
                pass

        else:
            # Verifica attributi
            if not hasattr(candidate, name):
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
    
    if errors['wrong_signature']:
        for name, expected, got in errors['wrong_signature']:
            error_messages.append(f"Firma errata per {name}: atteso {expected}, trovato {got}")
    
    if errors['missing_attributes']:
        error_messages.append(f"Attributi mancanti: {', '.join(errors['missing_attributes'])}")

    # Solleva eccezione
    if len(error_messages) == 1:
        raise BrokenImplementation(iface, error_messages[0])
    else:
        raise Invalid("\n".join(error_messages))
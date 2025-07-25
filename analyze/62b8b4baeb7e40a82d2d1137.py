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

    # Se non ci sono errori, restituisci True
    if not errors:
        return True

    # Gestione errori
    total_errors = sum(len(v) for v in errors.values())
    
    if total_errors == 1:
        # Caso speciale: un solo errore
        if errors['missing_methods']:
            raise BrokenImplementation(iface, errors['missing_methods'][0])
        if errors['not_callable']:
            raise BrokenMethodImplementation(iface, errors['not_callable'][0])
        if errors['wrong_signature']:
            name, expected, got = errors['wrong_signature'][0]
            raise BrokenMethodImplementation(iface, name, f"Expected {expected}, got {got}")
        if errors['missing_attributes']:
            raise BrokenImplementation(iface, errors['missing_attributes'][0])
    
    # Più errori: raccoglili tutti in un unico messaggio
    error_msg = []
    if errors['missing_methods']:
        error_msg.append(f"Missing methods: {', '.join(errors['missing_methods'])}")
    if errors['not_callable']:
        error_msg.append(f"Non-callable methods: {', '.join(errors['not_callable'])}")
    if errors['wrong_signature']:
        sig_errors = [f"{name} (expected {exp}, got {got})" for name, exp, got in errors['wrong_signature']]
        error_msg.append(f"Wrong signatures: {', '.join(sig_errors)}")
    if errors['missing_attributes']:
        error_msg.append(f"Missing attributes: {', '.join(errors['missing_attributes'])}")
    
    raise Invalid('\n'.join(error_msg))
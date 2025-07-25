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
                    errors['wrong_signature'].append(
                        (name, f"Expected {desc_sig}, got {impl_sig}")
                    )
            except ValueError:
                # Non è possibile ottenere la firma, lo ignoriamo
                pass

        else:
            # Verifica attributi
            try:
                getattr(candidate, name)
            except AttributeError:
                errors['missing_attributes'].append(name)

    # Gestione errori
    if not errors:
        return True

    # Se c'è un solo tipo di errore con una sola istanza
    total_errors = sum(len(v) for v in errors.values())
    if total_errors == 1:
        for error_type, instances in errors.items():
            if instances:
                if error_type == 'missing_methods':
                    raise BrokenImplementation(iface, instances[0])
                elif error_type == 'not_callable':
                    raise BrokenMethodImplementation(iface, instances[0])
                elif error_type == 'wrong_signature':
                    name, msg = instances[0]
                    raise BrokenMethodImplementation(iface, name, msg)
                elif error_type == 'missing_attributes':
                    raise BrokenImplementation(iface, instances[0])

    # Altrimenti, raccogliamo tutti gli errori
    error_msg = []
    if errors['missing_methods']:
        error_msg.append(f"Missing methods: {', '.join(errors['missing_methods'])}")
    if errors['not_callable']:
        error_msg.append(f"Non-callable methods: {', '.join(errors['not_callable'])}")
    if errors['wrong_signature']:
        error_msg.append(f"Wrong signatures: {'; '.join(f'{name}: {msg}' for name, msg in errors['wrong_signature'])}")
    if errors['missing_attributes']:
        error_msg.append(f"Missing attributes: {', '.join(errors['missing_attributes'])}")

    raise Invalid('\n'.join(error_msg))
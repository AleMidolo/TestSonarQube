def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        raise Invalid(f"{candidate!r} does not provide interface {iface!r}")

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Verify method exists
            if not hasattr(candidate, name):
                errors['missing_methods'].append(name)
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['not_callable'].append(name)
                continue

            # Verify method signature
            try:
                from inspect import signature
                impl_sig = signature(method)
                iface_sig = signature(desc)
                
                if impl_sig.parameters != iface_sig.parameters:
                    errors['wrong_signature'].append(name)
            except ValueError:
                # Can't get signature, skip check
                pass

        else:
            # Verify attribute exists
            if not hasattr(candidate, name):
                errors['missing_attributes'].append(name)

    # Raise errors if any found
    if errors:
        messages = []
        if errors['missing_methods']:
            messages.append(f"Missing required methods: {', '.join(errors['missing_methods'])}")
        if errors['not_callable']:
            messages.append(f"Attributes that should be methods: {', '.join(errors['not_callable'])}")
        if errors['wrong_signature']:
            messages.append(f"Methods with wrong signatures: {', '.join(errors['wrong_signature'])}")
        if errors['missing_attributes']:
            messages.append(f"Missing required attributes: {', '.join(errors['missing_attributes'])}")

        if len(messages) == 1:
            raise Invalid(messages[0])
        else:
            raise Invalid('\n'.join(messages))

    return True
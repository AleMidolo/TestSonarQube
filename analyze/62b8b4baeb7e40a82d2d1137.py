def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        raise DoesNotImplement(iface)

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(1):
        try:
            attr = getattr(candidate, name)
        except AttributeError:
            errors['missing_attributes'].append(
                f"The '{name}' attribute was not provided."
            )
            continue

        # If it's a method, verify the signature
        if isinstance(desc, Method):
            if not callable(attr):
                errors['invalid_methods'].append(
                    f"The '{name}' attribute is not callable but should be."
                )
                continue

            # Check method signature
            try:
                desc.getSignatureInfo()
            except ValueError as e:
                errors['signature_errors'].append(
                    f"Invalid signature for '{name}': {str(e)}"
                )

    # If we have any errors, raise them
    if errors:
        if sum(len(v) for v in errors.values()) == 1:
            # Special case: only one error, raise it directly
            error_msg = next(msg for msgs in errors.values() for msg in msgs)
            raise Invalid(error_msg)
        
        # Multiple errors: combine them all
        error_messages = []
        for error_type, messages in errors.items():
            if messages:
                error_messages.extend(messages)
        
        if error_messages:
            raise Invalid('\n'.join(error_messages))

    return True
def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['provided'].append(
            f"{candidate!r} does not provide interface {iface!r}"
        )

    # Check methods
    for name, desc in iface.namesAndDescriptions(all=True):
        if not isinstance(desc, Method):
            # Skip attributes
            continue

        # Check if method exists
        try:
            attr = getattr(candidate, name)
        except AttributeError:
            errors['methods'].append(
                f"The {name!r} method was not provided"
            )
            continue

        # Check if it's callable
        if not callable(attr):
            errors['methods'].append(
                f"The {name!r} object is not callable"
            )
            continue

        # Verify method signature if possible
        try:
            desc.getSignatureInfo()
        except ValueError:
            continue

        try:
            desc.validateSignature(attr)
        except Invalid as e:
            errors['signatures'].append(
                f"The signature of {name!r} is incorrect: {str(e)}"
            )

    # Check attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            continue

        try:
            getattr(candidate, name)
        except AttributeError:
            errors['attributes'].append(
                f"The {name!r} attribute was not provided"
            )

    # Raise errors if any found
    all_errors = [err for errs in errors.values() for err in errs]
    if len(all_errors) == 1:
        raise Invalid(all_errors[0])
    elif all_errors:
        raise Invalid('\n'.join(all_errors))

    return True
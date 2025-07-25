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

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Verify method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"The {name!r} method was not provided"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"The {name!r} attribute is not callable"
                )
                continue

            # Verify method signature
            try:
                desc.validateSignature(method)
            except Invalid as e:
                errors['signatures'].append(
                    f"The signature of {name!r} is incorrect: {str(e)}"
                )
        else:
            # Verify attribute exists
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"The {name!r} attribute was not provided"
                )

    # If no errors, return True
    if not errors:
        return True

    # Collect all errors
    all_errors = []
    for error_type, error_list in errors.items():
        all_errors.extend(error_list)

    # If only one error, raise it directly
    if len(all_errors) == 1:
        raise Invalid(all_errors[0])

    # If multiple errors, raise them all together
    if all_errors:
        raise Invalid('\n'.join(all_errors))

    return True
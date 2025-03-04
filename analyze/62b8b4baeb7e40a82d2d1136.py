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
            # Method verification
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"The {name!r} method was not provided by {candidate!r}"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"The {name!r} attribute of {candidate!r} is not callable"
                )
                continue

            # Verify method signature if possible
            try:
                import inspect
                expected_sig = inspect.signature(desc)
                actual_sig = inspect.signature(method)
                
                if expected_sig.parameters != actual_sig.parameters:
                    errors['signatures'].append(
                        f"The signature of {name!r} does not match the interface. "
                        f"Expected {expected_sig}, got {actual_sig}"
                    )
            except (ValueError, TypeError):
                pass  # Skip signature checking if not possible

        else:
            # Attribute verification 
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"The {name!r} attribute was not provided by {candidate!r}"
                )

    # If there are any errors, raise them
    if errors:
        all_errors = []
        for category, messages in errors.items():
            all_errors.extend(messages)
            
        if len(all_errors) == 1:
            raise Invalid(all_errors[0])
        else:
            raise Invalid('\n'.join(all_errors))

    return True
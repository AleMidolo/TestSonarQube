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
                f"The '{name}' attribute was not provided.")
            continue

        if isinstance(desc, Method):
            # Verify it's callable
            if not callable(attr):
                errors['invalid_methods'].append(
                    f"The '{name}' attribute is not callable.")
                continue

            # Check method signature
            import inspect
            expected = inspect.signature(desc)
            try:
                actual = inspect.signature(attr)
                if expected != actual:
                    errors['invalid_signatures'].append(
                        f"The '{name}' method has incorrect signature. "
                        f"Expected {expected}, got {actual}")
            except ValueError:
                errors['invalid_signatures'].append(
                    f"Could not inspect signature of '{name}' method.")

    # If we have any errors, raise them
    if errors:
        all_errors = []
        for error_type, messages in errors.items():
            all_errors.extend(messages)
            
        if len(all_errors) == 1:
            raise Invalid(all_errors[0])
        elif len(all_errors) > 1:
            raise Invalid("\n".join(all_errors))

    return True
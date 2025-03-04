def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['provide'].append(
            f"{candidate} does not provide interface {iface.__name__}"
        )

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Check if method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"Method {name} not provided by {candidate}"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"{name} is not callable on {candidate}"
                )
                continue

            # Check method signature if possible
            try:
                import inspect
                expected_sig = inspect.signature(desc)
                actual_sig = inspect.signature(method)
                
                if expected_sig.parameters != actual_sig.parameters:
                    errors['signatures'].append(
                        f"Method {name} has wrong signature: expected {expected_sig}, got {actual_sig}"
                    )
            except ValueError:
                pass  # Skip signature check if not possible

        else:
            # Check if attribute exists
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute {name} not provided by {candidate}"
                )

    # If no errors, return True
    if not errors:
        return True

    # Collect all error messages
    error_msgs = []
    for category, msgs in errors.items():
        error_msgs.extend(msgs)

    # If single error, raise it directly
    if len(error_msgs) == 1:
        raise Invalid(error_msgs[0])

    # If multiple errors, raise them all together
    if error_msgs:
        raise Invalid("\n".join(error_msgs))

    return True
from zope.interface import Invalid, providedBy
from inspect import signature

def _verify(iface, candidate, tentative=False, vtype=None):
    """
    Verify that the candidate correctly provides the interface.

    This includes:
    - Ensuring the candidate claims to provide the interface using `iface.providedBy`
      (unless tentative is True, in which case this step is skipped).
    - Ensuring the candidate defines all required methods.
    - Ensuring the methods have the correct signatures (as far as possible).
    - Ensuring the candidate defines all required attributes.

    :return bool: Returns a true value if all checks pass.
    :raises zope.interface.Invalid: If any of the above conditions are not met.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"{candidate} does not claim to provide {iface}.")

    # Step 2: Verify that the candidate defines all required methods
    required_methods = iface.namesAndDescriptions(all=True)
    for name, desc in required_methods:
        if not hasattr(candidate, name):
            errors.append(f"Method {name} is required but not implemented by {candidate}.")
        else:
            # Step 3: Verify method signatures (if possible)
            candidate_method = getattr(candidate, name)
            if callable(candidate_method):
                try:
                    candidate_sig = signature(candidate_method)
                    required_sig = signature(desc.getSignature())
                    if candidate_sig != required_sig:
                        errors.append(f"Method {name} has an incorrect signature. Expected {required_sig}, got {candidate_sig}.")
                except ValueError:
                    # If signature cannot be determined, skip this check
                    pass

    # Step 4: Verify that the candidate defines all required attributes
    required_attrs = iface.namesAndDescriptions(all=False)
    for name, desc in required_attrs:
        if not hasattr(candidate, name):
            errors.append(f"Attribute {name} is required but not defined by {candidate}.")

    # If there are any errors, raise an Invalid exception with all errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
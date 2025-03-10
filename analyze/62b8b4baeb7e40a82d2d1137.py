from zope.interface import Invalid, providedBy
from inspect import signature

def verifyObject(iface, candidate, tentative=False):
    """
    Verify that *candidate* might correctly provide *iface*.

    This involves:

    - Making sure the candidate claims that it provides the
      interface using ``iface.providedBy`` (unless *tentative* is `True`,
      in which case this step is skipped). This means that the candidate's class
      declares that it `implements <zope.interface.implementer>` the interface,
      or the candidate itself declares that it `provides <zope.interface.provider>`
      the interface

    - Making sure the candidate defines all the necessary methods

    - Making sure the methods have the correct signature (to the
      extent possible)

    - Making sure the candidate defines all the necessary attributes

    :return bool: Returns a true value if everything that could be
       checked passed.
    :raises zope.interface.Invalid: If any of the previous
       conditions does not hold.

    .. versionchanged:: 5.0
        If multiple methods or attributes are invalid, all such errors
        are collected and reported. Previously, only the first error was reported.
        As a special case, if only one such error is present, it is raised
        alone, like before.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not claim to provide {iface}")

    # Step 2: Verify that the candidate defines all necessary methods
    for method_name in iface.names():
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue

        # Step 3: Verify method signatures
        candidate_method = getattr(candidate, method_name)
        iface_method = getattr(iface, method_name)
        try:
            candidate_sig = signature(candidate_method)
            iface_sig = signature(iface_method)
            if candidate_sig != iface_sig:
                errors.append(f"Method {method_name} has incorrect signature. Expected {iface_sig}, got {candidate_sig}")
        except ValueError:
            # If signature cannot be determined, skip signature check
            pass

    # Step 4: Verify that the candidate defines all necessary attributes
    for attr_name in iface.names(all=True):
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    # Handle errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
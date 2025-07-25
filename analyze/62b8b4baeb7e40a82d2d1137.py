from zope.interface import providedBy, verify
from zope.interface.exceptions import Invalid
from zope.interface.interface import Method, Attribute

def verifyObject(iface, candidate, tentative=False):
    """
    Verify that the candidate correctly provides the interface.

    This includes:

    - Ensuring that the candidate claims to provide the interface,
      using ``iface.providedBy`` (unless *tentative* is `True`,
      in which case this step is skipped). This means that the candidate's class
      declares that it implements the interface with `implements <zope.interface.implementer>`,
      or the candidate itself declares that it provides the interface
      with `provides <zope.interface.provider>`.

    - Ensuring that the candidate defines all required methods.

    - Ensuring that the method signatures are correct (as far as possible).

    - Ensuring that the candidate defines all required attributes.

    :return bool: Returns a truth value if all checks succeed.
    :raises zope.interface.Invalid: If any of the above conditions are not met.

    .. versionchanged:: 5.0
        If multiple methods or attributes are invalid, all errors are collected and reported.
        Previously, only the first error was reported. In a special case, if only one error exists,
        it is raised alone as before.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not claim to provide {iface}.")

    # Step 2: Verify that all required methods are defined
    for name, method in iface.namesAndDescriptions():
        if isinstance(method, Method):
            if not hasattr(candidate, name):
                errors.append(f"Method '{name}' is required but not implemented by {candidate}.")
            else:
                # Step 3: Verify method signatures (as far as possible)
                candidate_method = getattr(candidate, name)
                if not callable(candidate_method):
                    errors.append(f"'{name}' is not a callable method in {candidate}.")
                else:
                    # Basic signature check (number of arguments)
                    expected_args = method.getSignatureInfo()['args']
                    actual_args = candidate_method.__code__.co_argcount
                    if actual_args < len(expected_args):
                        errors.append(f"Method '{name}' in {candidate} has fewer arguments than required.")

    # Step 4: Verify that all required attributes are defined
    for name, attribute in iface.namesAndDescriptions():
        if isinstance(attribute, Attribute):
            if not hasattr(candidate, name):
                errors.append(f"Attribute '{name}' is required but not defined by {candidate}.")

    # Raise collected errors or return True if no errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))
    return True
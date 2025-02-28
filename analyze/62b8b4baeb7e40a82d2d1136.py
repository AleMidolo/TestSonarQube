from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject, verifyClass

def _verify(iface, candidate, tentative=False, vtype=None):
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

    # Step 2: Verify that the candidate defines all necessary methods and attributes
    try:
        if vtype == 'class':
            verifyClass(iface, candidate)
        else:
            verifyObject(iface, candidate)
    except Invalid as e:
        errors.append(str(e))

    # Step 3: Handle errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True
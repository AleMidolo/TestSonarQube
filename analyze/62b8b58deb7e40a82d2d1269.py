def directlyProvidedBy(object): # pylint:disable=redefined-builtin
    """
    दिए गए ऑब्जेक्ट द्वारा सीधे प्रदान किए गए इंटरफ़ेस लौटाता है

    लौटाया गया मान `~zope.interfaces.interfaces.ideclaration` है।
    """
    from zope.interface.declarations import Provides, directlyProvides
    from zope.interface.interface import InterfaceClass
    
    # Get the __provides__ attribute if it exists
    provides = getattr(object, "__provides__", None)
    
    if provides is None:
        # If no specification exists, return empty declaration
        return Provides(type(object))
        
    # If it's a class, remove class-level declarations
    if isinstance(object, type):
        implements = provides._implements
        if implements is not None:
            provides = provides - implements

    return provides
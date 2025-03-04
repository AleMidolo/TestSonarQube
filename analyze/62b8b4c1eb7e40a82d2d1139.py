def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    # Get all attributes defined in the interface
    required_attrs = dir(iface)
    
    # Filter out private/special attributes
    required_attrs = [attr for attr in required_attrs if not attr.startswith('_')]
    
    # Check each required attribute
    for attr in required_attrs:
        # Check if attribute exists in candidate
        if not hasattr(candidate, attr):
            if tentative:
                return False
            raise AttributeError(f"'{candidate.__name__}' missing required attribute '{attr}'")
            
        # Get the interface and candidate attributes
        iface_attr = getattr(iface, attr)
        candidate_attr = getattr(candidate, attr)
        
        # If attribute is a method, verify signature matches
        if callable(iface_attr):
            if not callable(candidate_attr):
                if tentative:
                    return False
                raise TypeError(f"'{attr}' must be callable")
                
            # Compare number of arguments
            from inspect import signature
            iface_sig = signature(iface_attr)
            candidate_sig = signature(candidate_attr)
            
            if len(iface_sig.parameters) != len(candidate_sig.parameters):
                if tentative:
                    return False
                raise TypeError(f"'{attr}' has incorrect number of parameters")
                
    return True
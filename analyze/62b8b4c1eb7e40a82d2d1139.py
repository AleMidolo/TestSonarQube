def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
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
        
        # Check if attribute is a method
        if callable(iface_attr):
            if not callable(candidate_attr):
                if tentative:
                    return False
                raise TypeError(f"'{attr}' must be callable")
                
            # Check method signature matches
            iface_sig = str(iface_attr.__code__.co_varnames)
            candidate_sig = str(candidate_attr.__code__.co_varnames)
            if iface_sig != candidate_sig:
                if tentative:
                    return False
                raise TypeError(f"Method signature mismatch for '{attr}'")
                
    return True
def _resolve_string(matcher):
    """
    Ottieni il valore dall'ambiente dato un matcher che contiene un nome e un valore predefinito opzionale.  
    Se la variabile non è definita nell'ambiente e non viene fornito alcun valore predefinito, viene generato un errore.
    """
    import os
    
    # Extract variable name and default value from matcher
    var_name = matcher.group(1) if matcher.group(1) else matcher.group(0)
    default_value = matcher.group(2) if len(matcher.groups()) > 1 else None
    
    # Try to get value from environment
    value = os.environ.get(var_name)
    
    # If value not found in environment
    if value is None:
        # If default provided, use it
        if default_value is not None:
            return default_value
        # Otherwise raise error
        raise KeyError(f"Environment variable '{var_name}' not found and no default value provided")
        
    return value
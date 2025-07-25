def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    import os
    
    # Split matcher into name and default value (if provided)
    parts = matcher.split(':-')
    var_name = parts[0].strip()
    default_value = parts[1].strip() if len(parts) > 1 else None
    
    # Get value from environment
    value = os.environ.get(var_name)
    
    # Return value if found in environment
    if value is not None:
        return value
        
    # Return default if provided
    if default_value is not None:
        return default_value
        
    # Raise error if no value found and no default provided
    raise ValueError(f"Environment variable '{var_name}' not found and no default value provided")
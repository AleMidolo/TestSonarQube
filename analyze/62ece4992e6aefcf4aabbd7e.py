def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    import os
    
    # Split matcher into name and default value if present
    parts = matcher.split(':-')
    name = parts[0].strip()
    
    # Get default value if provided
    default = parts[1].strip() if len(parts) > 1 else None
    
    # Try to get value from environment
    value = os.environ.get(name)
    
    if value is None:
        if default is not None:
            return default
        else:
            raise ValueError(f"Environment variable '{name}' not found and no default value provided")
            
    return value
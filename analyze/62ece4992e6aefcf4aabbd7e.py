def _resolve_string(matcher):
    # Extract name and default value from matcher
    parts = matcher.group(1).split(':')
    name = parts[0]
    default = parts[1] if len(parts) > 1 else None

    # Get value from environment
    value = os.environ.get(name)
    
    # Return value if found
    if value is not None:
        return value
        
    # Return default if provided
    if default is not None:
        return default
        
    # Raise error if no value found and no default
    raise ValueError(f"Environment variable '{name}' not found and no default value provided")
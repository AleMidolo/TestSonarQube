import os

def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    name = matcher.get('name')
    default = matcher.get('default', None)
    
    value = os.getenv(name)
    
    if value is not None:
        return value
    elif default is not None:
        return default
    else:
        raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided.")
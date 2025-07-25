import os

def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    name, default_value = matcher.get('name'), matcher.get('default')
    
    value = os.getenv(name)
    
    if value is None:
        if default_value is not None:
            return default_value
        else:
            raise ValueError(f"Environment variable '{name}' is not defined and no default value provided.")
    
    return value
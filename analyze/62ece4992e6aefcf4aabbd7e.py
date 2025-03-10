import os

def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    name = matcher.get('name')
    default = matcher.get('default', None)
    
    if name not in os.environ:
        if default is None:
            raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided.")
        return default
    
    return os.environ[name]
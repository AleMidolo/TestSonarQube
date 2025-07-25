import os

def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    if not isinstance(matcher, dict):
        raise ValueError("matcher must be a dictionary containing 'name' and optionally 'default'")
    
    name = matcher.get('name')
    if not name:
        raise ValueError("matcher must contain a 'name' key")
    
    value = os.getenv(name)
    if value is not None:
        return value
    
    if 'default' in matcher:
        return matcher['default']
    
    raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided")
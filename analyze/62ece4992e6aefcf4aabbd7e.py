import os

def _resolve_string(matcher):
    name = matcher.group('name')
    default_value = matcher.group('default_value')
    
    value = os.getenv(name)
    
    if value is None:
        if default_value is not None:
            return default_value
        else:
            raise ValueError(f"Environment variable '{name}' is not defined and no default value provided.")
    
    return value
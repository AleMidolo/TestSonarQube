import os

def _resolve_string(matcher):
    """
    Obtener el valor del entorno dado un matcher que contiene un nombre y un valor predeterminado opcional.  
    Si la variable no está definida en el entorno y no se proporciona un valor predeterminado, se genera un Error.
    """
    name, default = matcher.group(1), matcher.group(2)
    value = os.getenv(name)
    
    if value is not None:
        return value
    elif default is not None:
        return default
    else:
        raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided.")
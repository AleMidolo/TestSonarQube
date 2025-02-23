import os

def _resolve_string(matcher):
    """
    Obtener el valor del entorno dado un matcher que contiene un nombre y un valor predeterminado opcional.  
    Si la variable no está definida en el entorno y no se proporciona un valor predeterminado, se genera un Error.
    """
    name = matcher.get('name')
    default_value = matcher.get('default', None)
    
    value = os.getenv(name, default_value)
    
    if value is None:
        raise ValueError(f"La variable de entorno '{name}' no está definida y no se proporcionó un valor predeterminado.")
    
    return value
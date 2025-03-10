import os

def _resolve_string(matcher):
    """
    Obtener el valor del entorno dado un matcher que contiene un nombre y un valor predeterminado opcional.  
    Si la variable no está definida en el entorno y no se proporciona un valor predeterminado, se genera un Error.
    """
    if not matcher:
        raise ValueError("El matcher no puede estar vacío.")
    
    parts = matcher.split(':')
    var_name = parts[0].strip()
    default_value = None if len(parts) == 1 else parts[1].strip()
    
    value = os.getenv(var_name, default_value)
    
    if value is None:
        raise ValueError(f"La variable de entorno '{var_name}' no está definida y no se proporcionó un valor predeterminado.")
    
    return value
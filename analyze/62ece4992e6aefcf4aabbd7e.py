import os

def _resolve_string(matcher):
    """
    Ottieni il valore dall'ambiente dato un matcher che contiene un nome e un valore predefinito opzionale.  
    Se la variabile non è definita nell'ambiente e non viene fornito alcun valore predefinito, viene generato un errore.
    """
    if not isinstance(matcher, str):
        raise ValueError("Il matcher deve essere una stringa.")
    
    parts = matcher.split(":")
    var_name = parts[0].strip()
    default_value = parts[1].strip() if len(parts) > 1 else None
    
    value = os.getenv(var_name)
    
    if value is not None:
        return value
    elif default_value is not None:
        return default_value
    else:
        raise ValueError(f"La variabile '{var_name}' non è definita nell'ambiente e non è stato fornito un valore predefinito.")
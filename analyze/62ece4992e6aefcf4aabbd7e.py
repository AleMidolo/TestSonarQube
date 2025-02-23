import os

def _resolve_string(matcher):
    """
    Ottieni il valore dall'ambiente dato un matcher che contiene un nome e un valore predefinito opzionale.  
    Se la variabile non è definita nell'ambiente e non viene fornito alcun valore predefinito, viene generato un errore.
    """
    name, default_value = matcher.get('name'), matcher.get('default')
    
    value = os.getenv(name)
    
    if value is None:
        if default_value is not None:
            return default_value
        else:
            raise ValueError(f"Environment variable '{name}' is not defined and no default value provided.")
    
    return value
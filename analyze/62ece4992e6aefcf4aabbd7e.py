import os

def _resolve_string(matcher):
    """
    Ottieni il valore dall'ambiente dato un matcher che contiene un nome e un valore predefinito opzionale.  
    Se la variabile non è definita nell'ambiente e non viene fornito alcun valore predefinito, viene generato un errore.
    """
    name, *default = matcher.groups()
    if name in os.environ:
        return os.environ[name]
    elif default:
        return default[0]
    else:
        raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided.")
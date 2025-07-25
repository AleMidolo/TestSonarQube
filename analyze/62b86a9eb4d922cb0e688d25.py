import re

def _get_resource_name_regex():
    """
    Crea o restituisci le espressioni regolari utilizzate per convalidare il nome delle risorse Krake.

    **Restituisce:**  
        `(re.Pattern)`: le espressioni regolari compilate, utilizzate per convalidare il nome della risorsa.
    """
    # Definisci il pattern per il nome della risorsa
    # Esempio: il nome deve iniziare con una lettera, seguito da lettere, numeri, trattini o underscore
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]*$'
    
    # Compila e restituisci il pattern
    return re.compile(pattern)
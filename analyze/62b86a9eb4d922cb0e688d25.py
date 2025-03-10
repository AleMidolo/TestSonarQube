import re

def _get_resource_name_regex():
    """
    Crea o restituisci le espressioni regolari utilizzate per convalidare il nome delle risorse Krake.

    **Restituisce:**  
        `(re.Pattern)`: le espressioni regolari compilate, utilizzate per convalidare il nome della risorsa.
    """
    # Definisci un pattern per convalidare il nome della risorsa
    # Esempio: solo lettere, numeri, trattini e underscore, con una lunghezza minima di 1 e massima di 63 caratteri
    pattern = r'^[a-zA-Z0-9-_]{1,63}$'
    
    # Compila e restituisci il pattern
    return re.compile(pattern)
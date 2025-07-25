import re

def _get_resource_name_regex():
    """
    Crea o restituisci le espressioni regolari utilizzate per convalidare il nome delle risorse Krake.

    **Restituisce:**  
        `(re.Pattern)`: le espressioni regolari compilate, utilizzate per convalidare il nome della risorsa.
    """
    # Definisci il pattern per convalidare il nome della risorsa
    # Esempio: solo lettere minuscole, numeri e trattini, lunghezza tra 1 e 63 caratteri
    pattern = r'^[a-z0-9-]{1,63}$'
    
    # Compila e restituisci il pattern
    return re.compile(pattern)
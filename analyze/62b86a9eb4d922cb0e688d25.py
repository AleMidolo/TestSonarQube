import re

def _get_resource_name_regex():
    """
    Crea o restituisci le espressioni regolari utilizzate per convalidare il nome delle risorse Krake.

    **Restituisce:**  
        `(re.Pattern)`: le espressioni regolari compilate, utilizzate per convalidare il nome della risorsa.
    """
    # Definisci un pattern per convalidare i nomi delle risorse Krake
    # Esempio: solo lettere minuscole, numeri e trattini, lunghezza tra 1 e 63 caratteri
    pattern = r'^[a-z0-9-]{1,63}$'
    return re.compile(pattern)
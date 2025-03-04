def _get_resource_name_regex():
    """
    Crea o restituisci le espressioni regolari utilizzate per convalidare il nome delle risorse Krake.

    **Restituisce:**  
        `(re.Pattern)`: le espressioni regolari compilate, utilizzate per convalidare il nome della risorsa.
    """
    import re
    
    # Pattern per nomi di risorse validi:
    # - Deve iniziare con una lettera minuscola
    # - Può contenere lettere minuscole, numeri e trattini
    # - Non può terminare con un trattino
    # - Lunghezza tra 1 e 63 caratteri
    pattern = r'^[a-z][a-z0-9-]{0,61}[a-z0-9]$'
    
    return re.compile(pattern)
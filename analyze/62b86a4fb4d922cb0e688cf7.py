def validate_key(key):
    """
    Valida la chiave fornita rispetto alla corrispondente espressione regolare.

    Argomenti:
        key: la stringa da validare

    Eccezioni:
        ValidationError: se la chiave fornita non è conforme all'espressione regolare.
    """
    import re

    class ValidationError(Exception):
        pass

    # Pattern per validare la chiave:
    # - Deve iniziare con una lettera
    # - Può contenere lettere, numeri e underscore
    # - Lunghezza minima 3, massima 32 caratteri
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,31}$'

    if not isinstance(key, str):
        raise ValidationError("La chiave deve essere una stringa")

    if not re.match(pattern, key):
        raise ValidationError("La chiave non è valida. Deve iniziare con una lettera, " 
                            "contenere solo lettere, numeri e underscore, "
                            "ed essere lunga tra 3 e 32 caratteri")

    return True
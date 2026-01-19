def _validate_name(self, name: str) -> str:
    """
    Valida il nome e lo restituisce. Se il nome è vuoto o supera i 33 caratteri di lunghezza, imposta a None.
    :param name: str, il nome da validare
    :return: str, il nome validato o None se non valido
    """
    if not name or len(name) > 33:
        return None
    return name
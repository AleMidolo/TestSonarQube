def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    Valida il numero di telefono e lo restituisce. Se phoneNumber è vuoto o non è un numero di 11 cifre, imposta a None.
    :param phoneNumber: str, il numero di telefono da validare
    :return: str, il numero di telefono validato o None se non valido
    """
    if not phoneNumber or not phoneNumber.isdigit() or len(phoneNumber) != 11:
        return None
    return phoneNumber
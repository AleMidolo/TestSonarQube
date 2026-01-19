def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
        Valida el número de teléfono y lo devuelve. Si phoneNumber está vacío o no es un número de 11 dígitos, se establece en None.
        :param phoneNumber: str, el número de teléfono a validar
        :return: str, el número de teléfono validado o None si es inválido
        """
    if not phoneNumber:
        return None
    if not phoneNumber.isdigit():
        return None
    if len(phoneNumber) != 11:
        return None
    return phoneNumber
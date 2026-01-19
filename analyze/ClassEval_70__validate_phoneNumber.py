def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    Valida el número de teléfono y lo devuelve. Si phoneNumber está vacío o no es un número de 11 dígitos, se establece en None.
    :param phoneNumber: str, el número de teléfono a validar
    :return: str, el número de teléfono validado o None si es inválido
    """
    if not phoneNumber or not phoneNumber.strip():
        return None
    
    # Eliminar espacios en blanco
    cleaned_number = phoneNumber.strip()
    
    # Verificar si contiene solo dígitos y tiene exactamente 11 dígitos
    if cleaned_number.isdigit() and len(cleaned_number) == 11:
        return cleaned_number
    
    return None
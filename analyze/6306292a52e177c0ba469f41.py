def test_tag(tag: str) -> bool:
    """
    Prueba una palabra para determinar si puede ser aceptada como una etiqueta.
    
    Args:
        tag (str): La palabra que se desea probar como etiqueta.
    
    Returns:
        bool: True si la palabra es válida como etiqueta, False en caso contrario.
    """
    # Definir reglas para una etiqueta válida
    # Por ejemplo, la etiqueta debe tener al menos 3 caracteres y no contener espacios
    if len(tag) >= 3 and ' ' not in tag:
        return True
    return False
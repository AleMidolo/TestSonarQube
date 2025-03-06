def test_tag(tag: str) -> bool:
    """
    Prueba una palabra para determinar si puede ser aceptada como una etiqueta.
    
    Args:
        tag (str): La palabra que se desea probar como etiqueta.
    
    Returns:
        bool: True si la palabra es aceptada como etiqueta, False en caso contrario.
    """
    # Verifica que la etiqueta no esté vacía y que solo contenga letras y números
    if not tag:
        return False
    return tag.isalnum()
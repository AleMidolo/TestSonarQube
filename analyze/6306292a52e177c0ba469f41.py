def test_tag(tag: str) -> bool:
    """
    Prueba una palabra para determinar si puede ser aceptada como una etiqueta.
    
    Args:
        tag (str): La palabra que se desea probar como etiqueta.
    
    Returns:
        bool: True si la palabra es aceptada como etiqueta, False en caso contrario.
    """
    # Aquí puedes definir las reglas para aceptar una etiqueta
    # Por ejemplo, que no esté vacía, que no contenga espacios, etc.
    if not tag:
        return False
    if ' ' in tag:
        return False
    # Puedes agregar más condiciones según sea necesario
    return True
def test_tag(tag: str) -> bool:
    """
    Prueba una palabra para determinar si puede ser aceptada como una etiqueta.
    """
    # Verificar que no esté vacía
    if not tag:
        return False
        
    # Verificar que solo contenga caracteres alfanuméricos y guiones bajos
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    
    # Verificar cada caracter
    for char in tag:
        if char not in valid_chars:
            return False
            
    # Verificar que no empiece con número
    if tag[0].isdigit():
        return False
        
    return True
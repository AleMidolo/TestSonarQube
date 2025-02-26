def test_tag(tag: str) -> bool:
    """
    Prueba una palabra para determinar si puede ser aceptada como una etiqueta.
    """
    if not tag:
        return False
    if len(tag) > 20:
        return False
    if not tag.isalnum():
        return False
    return True
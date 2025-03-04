def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    if not tag:
        return False
    if len(tag) > 30:
        return False
    if any(char in tag for char in [' ', '#', '@']):
        return False
    return True
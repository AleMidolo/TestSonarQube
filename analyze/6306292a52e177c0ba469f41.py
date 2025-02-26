def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    if not tag:
        return False
    if len(tag) > 30:
        return False
    if not tag.isalnum() and not all(c in '-_' for c in tag):
        return False
    return True
def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    if not tag:
        return False
    if len(tag) > 20:
        return False
    if not tag.isalnum():
        return False
    return True
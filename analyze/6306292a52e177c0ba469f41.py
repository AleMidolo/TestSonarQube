def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    # Example criteria: tag must be alphanumeric and between 3 and 20 characters long
    if not tag.isalnum():
        return False
    if len(tag) < 3 or len(tag) > 20:
        return False
    return True
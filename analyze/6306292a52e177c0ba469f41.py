def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    # Define a set of allowed characters (alphanumeric and underscore)
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    
    # Check if the tag is not empty and all characters are allowed
    if not tag:
        return False
    for char in tag:
        if char not in allowed_chars:
            return False
    return True
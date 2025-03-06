def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    # Define a set of allowed characters for the tag
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    
    # Check if the tag is not empty and all characters are allowed
    if not tag:
        return False
    return all(char in allowed_chars for char in tag)
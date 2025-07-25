def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    """
    # Check if tag is empty or contains only whitespace
    if not tag or tag.isspace():
        return False
        
    # Check if tag contains only alphanumeric chars and underscores
    if not tag.replace('_','').isalnum():
        return False
        
    # Check if tag starts with a letter
    if not tag[0].isalpha():
        return False
        
    # Check if tag is all lowercase
    if not tag.islower():
        return False
        
    return True
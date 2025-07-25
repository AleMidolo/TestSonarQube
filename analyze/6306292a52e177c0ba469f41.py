def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    # Check if tag is empty
    if not tag:
        return False
        
    # Check if tag contains only alphanumeric chars and hyphens
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(char in valid_chars for char in tag):
        return False
        
    # Check if tag starts or ends with hyphen
    if tag[0] == '-' or tag[-1] == '-':
        return False
        
    # Check if tag has consecutive hyphens
    if '--' in tag:
        return False
        
    return True
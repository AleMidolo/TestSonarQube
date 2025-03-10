def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    
    A tag is considered valid if it meets the following criteria:
    - It is not empty.
    - It contains only alphanumeric characters and underscores.
    - It is not longer than 50 characters.
    
    Args:
        tag (str): The word to be tested as a tag.
    
    Returns:
        bool: True if the tag is valid, False otherwise.
    """
    if not tag:
        return False
    if len(tag) > 50:
        return False
    if not tag.replace("_", "").isalnum():
        return False
    return True
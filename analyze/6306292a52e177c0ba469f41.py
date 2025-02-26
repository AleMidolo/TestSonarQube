def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    if not tag:
        return False
    if len(tag) > 20:
        return False
    if not tag.isalnum():
        return False
    return True
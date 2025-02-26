def test_tag(tag: str) -> bool:
    """
    Test a word whether it could be accepted as a tag.
    """
    if not tag:
        return False
    if len(tag) > 30:
        return False
    if not tag.isalnum() and '_' not in tag:
        return False
    return True
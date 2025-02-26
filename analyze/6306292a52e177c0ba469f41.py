def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    if not tag or not isinstance(tag, str):
        return False
    if len(tag) > 30 or len(tag) < 1:
        return False
    if not tag.isalnum() and not all(char in ['-', '_'] for char in tag):
        return False
    return True
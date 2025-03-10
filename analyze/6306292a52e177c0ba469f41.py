def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    # Check if the tag is not empty and contains only alphanumeric characters and underscores
    if not tag:
        return False
    for char in tag:
        if not (char.isalnum() or char == '_'):
            return False
    return True
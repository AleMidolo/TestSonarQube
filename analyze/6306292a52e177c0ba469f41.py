def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    if not tag:
        return False
    if len(tag) > 20:
        return False
    if not tag.isalnum():
        return False
    return True
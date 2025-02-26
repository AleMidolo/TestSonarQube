def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    if not tag:
        return False
    if not isinstance(tag, str):
        return False
    if any(char in tag for char in [' ', '#', '@', '!', '$', '%', '^', '&', '*', '(', ')']):
        return False
    return True
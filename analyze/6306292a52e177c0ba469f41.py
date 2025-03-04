def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    # Check if tag is empty
    if not tag:
        return False
        
    # Check if tag contains only alphanumeric chars and underscores
    if not all(c.isalnum() or c == '_' for c in tag):
        return False
        
    # Check if tag starts with letter
    if not tag[0].isalpha():
        return False
        
    # Check length is between 2 and 30 chars
    if len(tag) < 2 or len(tag) > 30:
        return False
        
    return True
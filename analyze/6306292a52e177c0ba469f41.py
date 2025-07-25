def test_tag(tag: str) -> bool:
    """
    किसी शब्द का परीक्षण करें कि क्या उसे टैग के रूप में स्वीकार किया जा सकता है।
    """
    # टैग के लिए मान्यता की शर्तें:
    # 1. टैग खाली नहीं होना चाहिए।
    # 2. टैग में केवल अक्षर, संख्याएं, और अंडरस्कोर (_) हो सकते हैं।
    # 3. टैग की लंबाई 1 से 50 वर्णों के बीच होनी चाहिए।
    
    if not tag:
        return False
    
    if not tag.isalnum() and '_' not in tag:
        return False
    
    if len(tag) < 1 or len(tag) > 50:
        return False
    
    return True
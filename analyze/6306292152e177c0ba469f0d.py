from typing import Union

def identify_request(request: Union[str, dict, list]) -> bool:
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि क्या यह एक मैट्रिक्स (Matrix) अनुरोध है।
    
    Args:
        request: यह एक स्ट्रिंग, डिक्शनरी, या लिस्ट हो सकता है जो अनुरोध को दर्शाता है।
    
    Returns:
        bool: यदि अनुरोध एक मैट्रिक्स है तो True, अन्यथा False।
    """
    if isinstance(request, list):
        # Check if all elements are lists (2D matrix)
        if all(isinstance(row, list) for row in request):
            return True
    return False
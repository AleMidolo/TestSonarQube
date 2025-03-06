from typing import Union

def identify_request(request: Union[str, dict, list]) -> bool:
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि क्या यह एक मैट्रिक्स (Matrix) अनुरोध है।
    
    Args:
        request (Union[str, dict, list]): अनुरोध जिसे जांचना है।
    
    Returns:
        bool: True यदि अनुरोध एक मैट्रिक्स है, अन्यथा False।
    """
    if isinstance(request, list):
        if all(isinstance(row, list) for row in request):
            return True
    return False
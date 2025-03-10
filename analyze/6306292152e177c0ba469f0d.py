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
        # Check if all elements are lists (2D matrix)
        if all(isinstance(row, list) for row in request):
            return True
        # Check if all elements are numbers (1D matrix)
        elif all(isinstance(element, (int, float)) for element in request):
            return True
    elif isinstance(request, dict):
        # Check if the dictionary contains matrix-like structure
        if all(isinstance(key, str) and isinstance(value, list) for key, value in request.items()):
            return True
    elif isinstance(request, str):
        # Check if the string represents a matrix (e.g., JSON or CSV format)
        try:
            import json
            data = json.loads(request)
            return identify_request(data)
        except json.JSONDecodeError:
            pass
    return False
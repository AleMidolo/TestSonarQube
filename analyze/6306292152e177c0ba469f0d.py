from typing import Union, List

RequestType = Union[str, List[List[int]]]

def identify_request(request: RequestType) -> bool:
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि क्या यह एक मैट्रिक्स (Matrix) अनुरोध है।
    """
    if isinstance(request, list):
        if all(isinstance(row, list) for row in request):
            return True
    return False
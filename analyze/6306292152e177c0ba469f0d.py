from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    # Assuming RequestType has a 'headers' attribute that is a dictionary
    if hasattr(request, 'headers'):
        headers = request.headers
        # Check for a specific header that indicates a Matrix request
        if 'X-Matrix-Request' in headers:
            return True
    return False
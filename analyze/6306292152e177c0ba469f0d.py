from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    # Assuming RequestType has a 'headers' attribute that is a dictionary
    if hasattr(request, 'headers'):
        headers = request.headers
        # Check for common Matrix request headers
        if 'Authorization' in headers and headers['Authorization'].startswith('Bearer '):
            return True
        if 'Content-Type' in headers and headers['Content-Type'] == 'application/json':
            return True
    return False
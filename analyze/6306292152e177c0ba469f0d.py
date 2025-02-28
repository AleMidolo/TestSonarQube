from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming RequestType has a 'headers' attribute that is a dictionary
    if hasattr(request, 'headers'):
        headers = request.headers
        # Check for a common Matrix header
        if 'Authorization' in headers and headers['Authorization'].startswith('Bearer '):
            return True
    return False
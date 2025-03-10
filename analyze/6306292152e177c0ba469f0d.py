from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    """
    # Assuming RequestType has a 'headers' attribute that contains the request headers
    if hasattr(request, 'headers'):
        headers = request.headers
        # Check for a specific header that indicates a Matrix request
        if 'Authorization' in headers and headers['Authorization'].startswith('Bearer '):
            # Further checks can be added here to validate the token or other headers
            return True
    return False
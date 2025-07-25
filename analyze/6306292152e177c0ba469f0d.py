from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming a Matrix request has a specific header or attribute
    if hasattr(request, 'headers'):
        return 'Matrix' in request.headers.get('User-Agent', '')
    return False
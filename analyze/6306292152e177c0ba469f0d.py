from typing import TypeVar

RequestType = TypeVar('RequestType')

def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming RequestType has a method or attribute to check if it's a Matrix request
    if hasattr(request, 'is_matrix_request'):
        return request.is_matrix_request()
    else:
        # Default to False if the request type doesn't support the check
        return False
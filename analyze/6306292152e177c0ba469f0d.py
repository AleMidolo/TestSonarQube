from typing import Union

def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    """
    # Assuming RequestType is a dictionary or object with a 'type' attribute/key
    if isinstance(request, dict):
        return request.get('type') == 'matrix'
    elif hasattr(request, 'type'):
        return request.type == 'matrix'
    return False
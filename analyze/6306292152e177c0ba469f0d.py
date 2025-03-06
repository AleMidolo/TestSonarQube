from typing import Union

def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    
    Args:
        request (RequestType): La richiesta da identificare.
    
    Returns:
        bool: True se la richiesta è di tipo Matrix, False altrimenti.
    """
    # Assuming RequestType has a 'type' attribute that indicates the type of request
    if hasattr(request, 'type'):
        return request.type == 'Matrix'
    return False
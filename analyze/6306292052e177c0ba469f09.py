from typing import Union

def identify_request(request: RequestType) -> Union[str, None]:
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    # Check for public message
    if hasattr(request, 'public_message') and request.public_message:
        return "Public message"
    
    # Check for private message
    elif hasattr(request, 'private_message') and request.private_message:
        return "Private message"
    
    # Check for legacy payload
    elif hasattr(request, 'legacy_payload') and request.legacy_payload:
        return "Legacy payload"
    
    # If none of the above, return None
    return None
def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    # Suponiendo que una solicitud de Matrix tiene un atributo 'type' que contiene 'matrix'
    return hasattr(request, 'type') and request.type == 'matrix'
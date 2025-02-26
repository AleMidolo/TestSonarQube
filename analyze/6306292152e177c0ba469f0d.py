def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    """
    # Assuming RequestType has an attribute 'type' that indicates the type of request
    return request.type.lower() == 'matrix'
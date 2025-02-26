def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    return isinstance(request, MatrixRequestType)  # Suponiendo que MatrixRequestType es el tipo de solicitud de Matrix
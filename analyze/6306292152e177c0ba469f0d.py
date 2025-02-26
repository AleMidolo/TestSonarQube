def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Matrix.
    """
    return isinstance(request, MatrixRequestType)  # Assuming MatrixRequestType is defined elsewhere
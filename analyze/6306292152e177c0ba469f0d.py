def identify_request(request: RequestType) -> bool:
    """
    Prova a identificare se si tratta di una richiesta Matrix.
    """
    return isinstance(request, MatrixRequestType)
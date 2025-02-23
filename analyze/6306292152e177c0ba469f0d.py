def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming Matrix requests have a specific attribute or structure
    return hasattr(request, 'matrix') and request.matrix is not None
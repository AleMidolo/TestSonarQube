def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # Assuming Matrix requests have a specific attribute or pattern
    return hasattr(request, 'matrix_id') or 'matrix' in request.url
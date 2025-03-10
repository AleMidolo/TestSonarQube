def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    # Check for public message
    if hasattr(request, 'public_message') and request.public_message:
        return "Public message identified"
    
    # Check for private message
    elif hasattr(request, 'private_message') and request.private_message:
        return "Private message identified"
    
    # Check for legacy payload
    elif hasattr(request, 'legacy_payload') and request.legacy_payload:
        return "Legacy payload identified"
    
    # If none of the above, return unknown
    return "Unknown request type"
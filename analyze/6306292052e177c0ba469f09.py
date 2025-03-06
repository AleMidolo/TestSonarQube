def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    # Check if it's a public message
    if hasattr(request, 'public_message'):
        return "Public message detected"
    
    # Check if it's a private message
    elif hasattr(request, 'private_message'):
        return "Private message detected"
    
    # Check if it's a legacy payload
    elif hasattr(request, 'legacy_payload'):
        return "Legacy payload detected"
    
    # If none of the above, return unknown
    else:
        return "Unknown request type"
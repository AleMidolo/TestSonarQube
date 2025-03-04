def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    # Check if it's a public message
    try:
        if request.get('entity_type') == 'Post' and request.get('public'):
            return 'public_message'
    except:
        pass

    # Check if it's a private message 
    try:
        if request.get('entity_type') == 'Message' and not request.get('public'):
            return 'private_message'
    except:
        pass

    # Check if it's a legacy payload
    try:
        if 'XML' in request.get('format', '') or request.get('legacy'):
            return 'legacy_payload'
    except:
        pass

    # If none of the above, return unknown
    return 'unknown'
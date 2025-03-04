def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    # Check if it's a public message
    if hasattr(request, 'public') and request.public:
        return 'public'
        
    # Check if it's a private message
    if hasattr(request, 'private') and request.private:
        return 'private'
        
    # Check if it's a legacy payload
    if hasattr(request, 'legacy_format'):
        return 'legacy'
        
    # If none of the above, return unknown
    return 'unknown'
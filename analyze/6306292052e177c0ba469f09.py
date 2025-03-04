def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    # Check if it's a public message
    try:
        if request.get('xml') is not None:
            return 'public'
    except:
        pass

    # Check if it's a private message
    try:
        if request.get('encrypted_magic_envelope') is not None:
            return 'private' 
    except:
        pass

    # Check if it's a legacy payload
    try:
        if request.get('legacy_xml_format') is not None:
            return 'legacy'
    except:
        pass

    # If none of the above, return unknown
    return 'unknown'
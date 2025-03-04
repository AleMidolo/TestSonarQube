def identify_request(request: RequestType):
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    if request.is_public_message():
        return "Public Message"
    elif request.is_private_message():
        return "Private Message"
    elif request.is_legacy_payload():
        return "Legacy Payload"
    else:
        return "Unknown Request"
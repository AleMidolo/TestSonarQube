def identify_request(request: RequestType):
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    if request.is_public_message():
        return "Public Message"
    elif request.is_private_message():
        return "Private Message"
    elif request.is_legacy_payload():
        return "Legacy Payload"
    else:
        return "Unknown Request"
def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. The check if this is a legacy payload.
    """
    if request.is_public_message():
        return "Public Message"
    elif request.is_private_message():
        return "Private Message"
    elif request.is_legacy_payload():
        return "Legacy Payload"
    else:
        return "Unknown Request"
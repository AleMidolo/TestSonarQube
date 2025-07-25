from typing import Union

def identify_request(request: RequestType) -> Union[str, None]:
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. Then check if this is a legacy payload.
    """
    if hasattr(request, 'public_message'):
        return "Public message detected"
    elif hasattr(request, 'private_message'):
        return "Private message detected"
    elif hasattr(request, 'legacy_payload'):
        return "Legacy payload detected"
    else:
        return None
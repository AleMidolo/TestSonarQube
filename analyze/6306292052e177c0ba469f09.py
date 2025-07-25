def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. Then check if this is a legacy payload.
    """
    if is_public_message(request):
        return "Public message"
    elif is_private_message(request):
        return "Private message"
    elif is_legacy_payload(request):
        return "Legacy payload"
    else:
        return "Unknown request type"

def is_public_message(request: RequestType) -> bool:
    """
    Check if the request is a public message.
    """
    # Implementation logic for checking public message
    return hasattr(request, 'public') and request.public

def is_private_message(request: RequestType) -> bool:
    """
    Check if the request is a private message.
    """
    # Implementation logic for checking private message
    return hasattr(request, 'private') and request.private

def is_legacy_payload(request: RequestType) -> bool:
    """
    Check if the request is a legacy payload.
    """
    # Implementation logic for checking legacy payload
    return hasattr(request, 'legacy') and request.legacy
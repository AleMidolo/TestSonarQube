from typing import Union

def identify_request(request: RequestType) -> Union[str, None]:
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. Then check if this is a legacy payload.

    Args:
        request (RequestType): The request to identify.

    Returns:
        Union[str, None]: Returns the type of request if identified, otherwise None.
    """
    # Check if it's a public message
    if hasattr(request, 'public_message') and request.public_message:
        return "public_message"
    
    # Check if it's a private message
    if hasattr(request, 'private_message') and request.private_message:
        return "private_message"
    
    # Check if it's a legacy payload
    if hasattr(request, 'legacy_payload') and request.legacy_payload:
        return "legacy_payload"
    
    # If none of the above, return None
    return None
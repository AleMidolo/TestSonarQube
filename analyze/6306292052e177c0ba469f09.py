def identify_request(request: RequestType):
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. The check if this is a legacy payload.
    """
    # First check if it's a public message
    if hasattr(request, 'public') and request.public:
        return 'public'
    
    # Then check if it's a private message
    if hasattr(request, 'private') and request.private:
        return 'private'
        
    # Check for legacy payload indicators
    if hasattr(request, 'xml_payload') or hasattr(request, 'legacy_format'):
        return 'legacy'
        
    # If none of the above, return None to indicate unidentified
    return None
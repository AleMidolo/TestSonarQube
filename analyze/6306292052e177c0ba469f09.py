def identify_request(request: RequestType):
    # Try to identify if it's a public message
    if isinstance(request, PublicMessage):
        return "public"
    
    # Try to identify if it's a private message
    if isinstance(request, PrivateMessage):
        return "private"
        
    # Check if it's a legacy payload
    if isinstance(request, LegacyPayload):
        return "legacy"
        
    # If none of the above, return unknown
    return "unknown"
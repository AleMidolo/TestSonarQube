def identify_request(request: RequestType):
    # Check for public message first
    if hasattr(request, 'public') and request.public:
        return 'public'
    
    # Then check for private message
    if hasattr(request, 'private') and request.private:
        return 'private'
        
    # Finally check if it's a legacy payload
    if hasattr(request, 'legacy_payload'):
        return 'legacy'
        
    # If none of the above, return None
    return None
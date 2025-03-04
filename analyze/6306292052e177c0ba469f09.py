def identify_request(request: RequestType):
    # Try to identify if it's a public message
    if hasattr(request, 'entity_type') and request.entity_type == 'status_message':
        return 'public'
        
    # Try to identify if it's a private message
    if hasattr(request, 'aes_key') or hasattr(request, 'encrypted_magic_envelope'):
        return 'private'
        
    # Check if it's a legacy payload by looking for old format indicators
    if hasattr(request, 'xml_payload') or hasattr(request, 'legacy_format'):
        return 'legacy'
        
    # If we can't identify the request type
    return 'unknown'
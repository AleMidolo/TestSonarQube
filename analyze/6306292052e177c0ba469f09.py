def identify_request(request: RequestType):
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    # Check if it's a public message
    if hasattr(request, 'public') and request.public:
        return 'public'
        
    # Check if it's a private message
    if hasattr(request, 'private') and request.private:
        return 'private'
        
    # Check if it's a legacy payload
    if hasattr(request, 'legacy') and request.legacy:
        return 'legacy'
        
    # If none of the above, return None
    return None
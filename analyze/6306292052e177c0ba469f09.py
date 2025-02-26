def identify_request(request: RequestType):
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    if is_public_message(request):
        return "Public message identified"
    elif is_private_message(request):
        return "Private message identified"
    elif is_legacy_payload(request):
        return "Legacy payload identified"
    else:
        return "Unknown request type"

def is_public_message(request):
    # Logic to determine if the request is a public message
    return hasattr(request, 'public') and request.public

def is_private_message(request):
    # Logic to determine if the request is a private message
    return hasattr(request, 'private') and request.private

def is_legacy_payload(request):
    # Logic to determine if the request is a legacy payload
    return hasattr(request, 'legacy') and request.legacy
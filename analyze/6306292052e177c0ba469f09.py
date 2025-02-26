def identify_request(request: RequestType):
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    if is_public_message(request):
        return "Public Message"
    elif is_private_message(request):
        return "Private Message"
    elif is_legacy_payload(request):
        return "Legacy Payload"
    else:
        return "Unknown Request"

def is_public_message(request):
    # Implementación para verificar si es un mensaje público
    return hasattr(request, 'public') and request.public

def is_private_message(request):
    # Implementación para verificar si es un mensaje privado
    return hasattr(request, 'private') and request.private

def is_legacy_payload(request):
    # Implementación para verificar si es una carga útil heredada
    return hasattr(request, 'legacy') and request.legacy
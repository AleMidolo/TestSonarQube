from enum import Enum

class RequestType(Enum):
    PUBLIC_MESSAGE = 1
    PRIVATE_MESSAGE = 2
    LEGACY_PAYLOAD = 3

def identify_request(request: RequestType):
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    if request == RequestType.PUBLIC_MESSAGE:
        return "Es una solicitud de Diaspora: Mensaje público."
    elif request == RequestType.PRIVATE_MESSAGE:
        return "Es una solicitud de Diaspora: Mensaje privado."
    elif request == RequestType.LEGACY_PAYLOAD:
        return "Es una solicitud de Diaspora: Carga útil heredada."
    else:
        return "No se pudo identificar la solicitud."
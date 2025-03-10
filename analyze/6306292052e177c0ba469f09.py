from enum import Enum

class RequestType(Enum):
    PUBLIC_MESSAGE = 1
    PRIVATE_MESSAGE = 2
    LEGACY_PAYLOAD = 3

def identify_request(request: RequestType) -> bool:
    """
    Intente identificar si esta es una solicitud de Diaspora.

    Primero intente con un mensaje público. Luego con un mensaje privado. Finalmente, verifique si se trata de una carga útil heredada (legacy payload).
    """
    if request == RequestType.PUBLIC_MESSAGE:
        return True
    elif request == RequestType.PRIVATE_MESSAGE:
        return True
    elif request == RequestType.LEGACY_PAYLOAD:
        return True
    else:
        return False
from enum import Enum

class RequestType(Enum):
    PUBLIC_MESSAGE = 1
    PRIVATE_MESSAGE = 2
    LEGACY_PAYLOAD = 3
    UNKNOWN = 4

def identify_request(request: RequestType) -> str:
    """
    Prova a identificare se si tratta di una richiesta Diaspora.

    Prova prima con un messaggio pubblico. Poi con un messaggio privato. Infine, verifica se si tratta di un payload legacy.
    """
    if request == RequestType.PUBLIC_MESSAGE:
        return "Richiesta Diaspora: Messaggio pubblico identificato."
    elif request == RequestType.PRIVATE_MESSAGE:
        return "Richiesta Diaspora: Messaggio privato identificato."
    elif request == RequestType.LEGACY_PAYLOAD:
        return "Richiesta Diaspora: Payload legacy identificato."
    else:
        return "Tipo di richiesta non riconosciuto."
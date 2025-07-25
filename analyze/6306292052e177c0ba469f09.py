from enum import Enum

class RequestType(Enum):
    PUBLIC_MESSAGE = 1
    PRIVATE_MESSAGE = 2
    LEGACY_PAYLOAD = 3
    UNKNOWN = 4

def identify_request(request: RequestType) -> str:
    """
    Try to identify whether this is a Diaspora request.

    Try first public message. Then private message. Then check if this is a legacy payload.
    """
    if request == RequestType.PUBLIC_MESSAGE:
        return "This is a public message request."
    elif request == RequestType.PRIVATE_MESSAGE:
        return "This is a private message request."
    elif request == RequestType.LEGACY_PAYLOAD:
        return "This is a legacy payload request."
    else:
        return "This request type is unknown."
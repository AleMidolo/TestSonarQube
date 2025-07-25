from enum import Enum

class RequestType(Enum):
    PUBLIC_MESSAGE = 1
    PRIVATE_MESSAGE = 2
    LEGACY_PAYLOAD = 3
    UNKNOWN = 4

def identify_request(request: RequestType) -> bool:
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि यह एक Diaspora अनुरोध है या नहीं।

    सबसे पहले सार्वजनिक संदेश (public message) की जांच करें। 
    फिर निजी संदेश (private message) की जांच करें। 
    अंत में यह जांचें कि क्या यह एक पुराना (legacy) payload है।
    """
    if request == RequestType.PUBLIC_MESSAGE:
        return True
    elif request == RequestType.PRIVATE_MESSAGE:
        return True
    elif request == RequestType.LEGACY_PAYLOAD:
        return True
    else:
        return False
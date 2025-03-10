from typing import Union

def identify_request(request: RequestType) -> Union[bool, str]:
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि यह एक Diaspora अनुरोध है या नहीं।

    सबसे पहले सार्वजनिक संदेश (public message) की जांच करें। 
    फिर निजी संदेश (private message) की जांच करें। 
    अंत में यह जांचें कि क्या यह एक पुराना (legacy) payload है।
    """
    
    # Check for public message
    if hasattr(request, 'public_message') and request.public_message:
        return "Public message detected"
    
    # Check for private message
    if hasattr(request, 'private_message') and request.private_message:
        return "Private message detected"
    
    # Check for legacy payload
    if hasattr(request, 'legacy_payload') and request.legacy_payload:
        return "Legacy payload detected"
    
    # If none of the above, return False
    return False
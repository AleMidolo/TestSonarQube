def identify_request(request: RequestType):
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि यह एक Diaspora अनुरोध है या नहीं।

    सबसे पहले सार्वजनिक संदेश (public message) की जांच करें। 
    फिर निजी संदेश (private message) की जांच करें। 
    अंत में यह जांचें कि क्या यह एक पुराना (legacy) payload है।
    """
    if request.is_public_message():
        return "Public Message"
    elif request.is_private_message():
        return "Private Message"
    elif request.is_legacy_payload():
        return "Legacy Payload"
    else:
        return "Unknown Request"
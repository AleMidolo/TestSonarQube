def identify_request(request: RequestType):
    """
    यह फ़ंक्शन यह पहचानने की कोशिश करता है कि यह एक Diaspora अनुरोध है या नहीं।

    सबसे पहले सार्वजनिक संदेश (public message) की जांच करें। 
    फिर निजी संदेश (private message) की जांच करें। 
    अंत में यह जांचें कि क्या यह एक पुराना (legacy) payload है।
    """
    if request.is_public_message():
        return "यह एक सार्वजनिक संदेश है।"
    elif request.is_private_message():
        return "यह एक निजी संदेश है।"
    elif request.is_legacy_payload():
        return "यह एक पुराना payload है।"
    else:
        return "यह कोई मान्य Diaspora अनुरोध नहीं है।"
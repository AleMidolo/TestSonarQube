def retrieve_diaspora_host_meta(host):
    """
    एक रिमोट डायस्पोरा होस्ट-मेटा डॉक्यूमेंट प्राप्त करें।

    :arg host: वह होस्ट जिससे डेटा प्राप्त करना है 
    :returns: ``XRD`` इंस्टेंस
    """
    import requests
    from xrd import XRD
    
    # Try HTTPS first
    try:
        url = f"https://{host}/.well-known/host-meta"
        response = requests.get(url)
        if response.status_code == 200:
            return XRD.parse_xrd(response.text)
    except:
        pass
        
    # Fall back to HTTP if HTTPS fails
    try:
        url = f"http://{host}/.well-known/host-meta"
        response = requests.get(url)
        if response.status_code == 200:
            return XRD.parse_xrd(response.text)
    except:
        pass
        
    raise ConnectionError(f"Could not retrieve host-meta from {host}")
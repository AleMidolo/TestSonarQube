def retrieve_diaspora_host_meta(host):
    """
    एक रिमोट डायस्पोरा होस्ट-मेटा डॉक्यूमेंट प्राप्त करें।

    :arg host: वह होस्ट जिससे डेटा प्राप्त करना है 
    :returns: ``XRD`` इंस्टेंस
    """
    import requests
    from xrd import XRD
    
    # Try HTTPS first, then fallback to HTTP if needed
    urls = [
        f"https://{host}/.well-known/host-meta",
        f"http://{host}/.well-known/host-meta"
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Parse XRD document from response
                xrd = XRD.parse_xrd(response.text)
                return xrd
        except requests.exceptions.RequestException:
            continue
            
    # If we get here, both HTTPS and HTTP failed
    raise Exception(f"Could not retrieve host-meta document from {host}")
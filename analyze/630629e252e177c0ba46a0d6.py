def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    import requests
    from xrd import XRD
    
    # Try HTTPS first, fall back to HTTP
    urls = [
        f"https://{host}/.well-known/host-meta",
        f"http://{host}/.well-known/host-meta"
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Parse XRD document from response content
                xrd = XRD.parse_xrd(response.content)
                return xrd
        except requests.RequestException:
            continue
            
    # If we get here, both attempts failed
    raise ValueError(f"Could not retrieve host-meta from {host}")
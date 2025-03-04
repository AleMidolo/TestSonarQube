def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento host-meta remoto di Diaspora.

    :arg host: Host da cui recuperare
    :returns: Istanza di ``XRD``
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
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Parse XRD document from response content
                xrd = XRD.parse_xrd(response.text)
                return xrd
        except (requests.RequestException, ValueError):
            continue
            
    # If we get here, both HTTPS and HTTP failed
    raise ConnectionError(f"Could not retrieve host-meta from {host}")
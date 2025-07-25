def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento "host-meta" remoto de Diaspora.

    :arg host: Host del cual se recuperará el documento
    :returns: Instancia de ``XRD``
    """
    import requests
    from xrd import XRD
    
    # URLs to try in order - first HTTPS then HTTP
    urls = [
        f"https://{host}/.well-known/host-meta",
        f"http://{host}/.well-known/host-meta"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Parse the XRD document from the response content
                xrd = XRD.parse_xrd(response.content)
                return xrd
        except (requests.RequestException, ValueError):
            continue
            
    # If we get here, both URLs failed
    raise ConnectionError(f"Could not retrieve host-meta from {host}")
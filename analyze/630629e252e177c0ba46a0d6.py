def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    import requests
    from lxml import etree

    # Construct the host-meta URL
    host_meta_url = f"https://{host}/host-meta"

    # Send a GET request to the host-meta URL
    response = requests.get(host_meta_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response content as XML
        xrd = etree.fromstring(response.content)
        return xrd
    else:
        response.raise_for_status()
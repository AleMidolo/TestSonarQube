def retrieve_diaspora_host_meta(host):
    """
    检索远程 Diaspora 的 host-meta 文档。

    :arg host: 要检索的主机
    :returns: ``XRD`` 实例
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
        xrd_content = etree.fromstring(response.content)
        return xrd_content
    else:
        response.raise_for_status()
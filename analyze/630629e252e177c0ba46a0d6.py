def retrieve_diaspora_host_meta(host):
    """
    检索远程 Diaspora 的 host-meta 文档。

    :arg host: 要检索的主机
    :returns: ``XRD`` 实例
    """
    import requests
    from lxml import etree

    url = f"https://{host}/host-meta"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve host-meta for {host}: {response.status_code}")

    xrd = etree.fromstring(response.content)
    return xrd
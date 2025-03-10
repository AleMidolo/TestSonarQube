import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    检索远程 Diaspora 的 host-meta 文档。

    :arg host: 要检索的主机
    :returns: ``XRD`` 实例
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the XML response
    xml_root = etree.fromstring(response.content)
    
    # Return the parsed XRD instance
    return xml_root
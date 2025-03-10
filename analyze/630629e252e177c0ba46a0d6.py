import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento host-meta remoto di Diaspora.

    :arg host: Host da cui recuperare
    :returns: Istanza di ``XRD``
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the XML response into an XRD instance
    xml_content = response.content
    xrd = etree.fromstring(xml_content)
    
    return xrd
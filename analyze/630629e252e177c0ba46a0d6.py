import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento "host-meta" remoto de Diaspora.

    :arg host: Host del cual se recuperará el documento
    :returns: Instancia de ``XRD``
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the XML response into an XRD instance
    xml_tree = etree.fromstring(response.content)
    return xml_tree
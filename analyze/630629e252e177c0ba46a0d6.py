import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the XML response
    xml_root = etree.fromstring(response.content)
    
    # Assuming XRD is a class that can be initialized with the XML root
    return XRD(xml_root)

# Assuming XRD is a class that can be initialized with an XML root
class XRD:
    def __init__(self, xml_root):
        self.xml_root = xml_root
        # Additional parsing logic can be added here
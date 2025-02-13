import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Recupera un documento host-meta remoto di Diaspora.

    :arg host: Host da cui recuperare
    :returns: Istanza di ``XRD``
    """
    url = f"https://{host}/host-meta"
    response = requests.get(url)
    
    if response.status_code == 200:
        xrd = etree.fromstring(response.content)
        return xrd
    else:
        response.raise_for_status()
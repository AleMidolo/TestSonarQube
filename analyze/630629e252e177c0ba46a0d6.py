import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    response = requests.get(f"{host}/host-meta")
    response.raise_for_status()
    xrd = etree.fromstring(response.content)
    return xrd
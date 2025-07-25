import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    एक रिमोट डायस्पोरा होस्ट-मेटा डॉक्यूमेंट प्राप्त करें।

    :arg host: वह होस्ट जिससे डेटा प्राप्त करना है
    :returns: ``XRD`` इंस्टेंस
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the XML response
    xml_tree = etree.fromstring(response.content)
    
    return xml_tree
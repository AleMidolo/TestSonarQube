import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    एक रिमोट डायस्पोरा होस्ट-मेटा डॉक्यूमेंट प्राप्त करें।

    :arg host: वह होस्ट जिससे डेटा प्राप्त करना है
    :returns: ``XRD`` इंस्टेंस
    """
    url = f"https://{host}/.well-known/webfinger?resource=acct:example@{host}"
    response = requests.get(url)
    
    if response.status_code == 200:
        xrd_data = response.text
        return etree.fromstring(xrd_data)
    else:
        response.raise_for_status()
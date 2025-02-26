def retrieve_diaspora_host_meta(host):
    """
    एक रिमोट डायस्पोरा होस्ट-मेटा डॉक्यूमेंट प्राप्त करें।

    :arg host: वह होस्ट जिससे डेटा प्राप्त करना है
    :returns: ``XRD`` इंस्टेंस
    """
    import requests
    from lxml import etree

    # Construct the URL for the host's meta document
    url = f"https://{host}/.well-known/host-meta"

    # Send a GET request to the host
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response content as XML
        xrd_content = response.content
        xrd_tree = etree.fromstring(xrd_content)
        return xrd_tree
    else:
        raise Exception(f"Failed to retrieve host meta for {host}: {response.status_code}")
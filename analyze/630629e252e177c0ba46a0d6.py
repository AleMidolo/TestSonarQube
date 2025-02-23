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

    try:
        # Send a GET request to the host
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the response content as XML
        xrd_content = response.content
        xrd_tree = etree.fromstring(xrd_content)

        # Return the parsed XRD instance
        return xrd_tree

    except requests.RequestException as e:
        print(f"Error retrieving host meta: {e}")
        return None
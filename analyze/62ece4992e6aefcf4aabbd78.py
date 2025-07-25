def is_local(host):
    """
    होस्ट की जाँच करता है कि क्या यह लोकलहोस्ट है।

    :param host: होस्टनाम या IP एड्रेस।
    :return: True यदि होस्ट लोकलहोस्ट है, अन्यथा False।
    """
    # List of common localhost hostnames and IPs
    localhost_values = [
        'localhost',
        '127.0.0.1',
        '::1',
        '0:0:0:0:0:0:0:1',
        '0.0.0.0'
    ]
    
    # Convert host to lowercase for case-insensitive comparison
    host = host.lower()
    
    # Check if host matches any localhost value
    return host in localhost_values
def is_local(host):
    """
    होस्ट की जाँच करता है कि क्या यह लोकलहोस्ट है।

    :param host: होस्टनाम या IP एड्रेस।
    :return: True यदि होस्ट लोकलहोस्ट है, अन्यथा False।
    """
    return host in ('localhost', '127.0.0.1', '::1')
def is_valid_ipv4(ip_address):
    """
    दिए गए IP पते की वैधता की जांच करें कि यह एक वैध IPv4 पता है या नहीं।
    :param ip_address: स्ट्रिंग, जांचने के लिए IP पता
    :return: बूल, यदि IP पता वैध है तो True, अन्यथा False
    >>> is_valid_ipv4('192.168.0.123')
    True
    >>> is_valid_ipv4('256.0.0.0')
    False

    """
    import socket
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except socket.error:
        return False
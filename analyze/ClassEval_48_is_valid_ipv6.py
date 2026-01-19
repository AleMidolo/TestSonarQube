@staticmethod
def is_valid_ipv6(ip_address):
    """
    जांचें कि दिया गया IP पता एक मान्य IPv6 पता है या नहीं।
    :param ip_address:string, जांचने के लिए IP पता
    :return:bool, यदि IP पता मान्य है तो True, अन्यथा False
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
    False

    """
    import socket
    
    try:
        # Try to convert the address using socket.inet_pton
        socket.inet_pton(socket.AF_INET6, ip_address)
        return True
    except (socket.error, OSError, ValueError, AttributeError):
        return False
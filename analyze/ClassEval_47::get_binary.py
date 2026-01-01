def get_binary(self):
    """
        यदि IP पता मान्य है, तो IP पते का बाइनरी रूप लौटाएं; अन्यथा, '' लौटाएं
        :return: स्ट्रिंग
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        return '.'.join((format(int(octet), '08b') for octet in self.ip_address.split('.')))
    else:
        return ''
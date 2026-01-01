def get_binary(self):
    """
        यदि IP पता मान्य है, तो IP पते का बाइनरी रूप लौटाएं; अन्यथा, '' लौटाएं
        :return: स्ट्रिंग
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        octets = self.get_octets()
        binary_octets = [format(int(octet), '08b') for octet in octets]
        return '.'.join(binary_octets)
    else:
        return ''
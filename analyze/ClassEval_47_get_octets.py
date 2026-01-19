def get_octets(self):
    """
        यदि IP पता मान्य है, तो IP पते का निर्माण करने वाले चार दशमलव संख्याओं की सूची जो "." द्वारा अलग की गई है, लौटाई जाती है; अन्यथा, एक खाली सूची लौटाई जाती है
        :return: सूची
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
    if self.is_valid():
        return self.ip_address.split('.')
    else:
        return []
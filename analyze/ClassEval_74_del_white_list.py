def del_white_list(self, addr):
    """
    एक पते को व्हाइटलिस्ट से हटा दें और यदि यह मौजूद नहीं है तो कुछ न करें
    :param addr: int, हटाने के लिए पता
    :return: नई व्हाइटलिस्ट, यदि पता मौजूद नहीं है तो False लौटाएं
    >>> server = Server()
    >>> server.add_white_list(88)
    >>> server.del_white_list(88)
    []
    """
    if addr not in self.white_list:
        return False
    else:
        self.white_list.remove(addr)
        return self.white_list
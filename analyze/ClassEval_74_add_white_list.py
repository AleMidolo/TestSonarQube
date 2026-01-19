def add_white_list(self, addr):
    """
    एक पते को व्हाइटलिस्ट में जोड़ें और यदि यह पहले से मौजूद है तो कुछ न करें
    :param addr: int, जो पता जोड़ा जाना है
    :return: नई व्हाइटलिस्ट, यदि पता पहले से मौजूद है तो False लौटाएं
    >>> server = Server()
    >>> server.add_white_list(88)
    [88]
    """
    if not hasattr(self, 'white_list'):
        self.white_list = []
    
    if addr in self.white_list:
        return False
    
    self.white_list.append(addr)
    return self.white_list
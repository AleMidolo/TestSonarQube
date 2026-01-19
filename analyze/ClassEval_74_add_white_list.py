def add_white_list(self, addr):
    """
    Add an address to the whitelist and do nothing if it already exists
    :param addr: int, address to be added
    :return: new whitelist, return False if the address already exists
    >>> server = Server()
    >>> server.add_white_list(88)
    [88]
    """
    if not hasattr(self, 'whitelist'):
        self.whitelist = []
    
    if addr in self.whitelist:
        return False
    
    self.whitelist.append(addr)
    return self.whitelist
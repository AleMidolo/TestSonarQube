def add_white_list(self, addr):
    """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
    if addr in self.white_list:
        return False
    else:
        self.white_list.append(addr)
        return self.white_list
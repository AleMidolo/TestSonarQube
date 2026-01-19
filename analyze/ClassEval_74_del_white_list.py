def del_white_list(self, addr):
    """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """
    if addr not in self.white_list:
        return False
    else:
        self.white_list.remove(addr)
        return self.white_list
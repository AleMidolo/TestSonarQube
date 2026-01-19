def add_white_list(self, addr):
    """
    将地址添加到白名单，如果已存在则不做任何操作
    :param addr: int, 要添加的地址
    :return: 新的白名单，如果地址已存在则返回 False
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
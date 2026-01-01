def del_white_list(self, addr):
    """
        从白名单中移除一个地址，如果该地址不存在则不执行任何操作
        :param addr: int, 要删除的地址
        :return: 新的白名单，如果地址不存在则返回 False
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """
    if addr not in self.white_list:
        return False
    else:
        self.white_list.remove(addr)
        return self.white_list
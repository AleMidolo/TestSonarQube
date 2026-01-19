def recv(self, info):
    """
    接收包含地址和内容的信息。如果地址在白名单上，则接收内容；否则，不接收
    :param info: dict，包含地址和内容的信息字典
    :return: 如果成功接收，返回信息的内容;否则,返回 False
    >>> server.recv({"addr":88,"content":"abc"})
    abc
    """
    if hasattr(self, 'whitelist') and info.get('addr') in self.whitelist:
        return info.get('content')
    return False
def recv(self, info):
    """
        Receive information containing address and content. If the address is in the whitelist, receive the content; otherwise, do not receive it.
        :param info: dict, information dictionary containing address and content
        :return: if received successfully, return the content of the information; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return False
    if info['addr'] in self.white_list:
        self.receive_struct = {'addr': info['addr'], 'content': info['content']}
        return info['content']
    return False
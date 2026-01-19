def send(self, info):
    """
        发送包含地址和内容的信息
        :param info: dict，包含地址和内容的信息字典
        :return: 如果成功发送，则返回无；否则，返回一个指示错误消息的字符串
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return 'Invalid input'
    addr = info['addr']
    content = info['content']
    self.send_struct = {'addr': addr, 'content': content}
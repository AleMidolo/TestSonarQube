def send(self, info):
    """
    发送包含地址和内容的信息
    :param info: dict，包含地址和内容的信息字典
    :return: 如果成功发送,则返回无;否则,返回一个指示错误消息的字符串
    >>> server.send({"addr":66,"content":"ABC"})
    self.send_struct = {"addr":66,"content":"ABC"}
    """
    try:
        if not isinstance(info, dict):
            return "错误: 参数必须是字典类型"
        
        if "addr" not in info:
            return "错误: 缺少地址(addr)字段"
        
        if "content" not in info:
            return "错误: 缺少内容(content)字段"
        
        self.send_struct = info
        return None
    except Exception as e:
        return f"错误: {str(e)}"
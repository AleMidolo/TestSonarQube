def send(self, info):
    """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return "Error: Invalid info format. Must be a dict with 'addr' and 'content' keys."
    self.send_struct = {'addr': info['addr'], 'content': info['content']}
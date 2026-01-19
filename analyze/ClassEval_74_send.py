def send(self, info):
    """
    Send information containing address and content
    :param info: dict, information dictionary containing address and content
    :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
    >>> server.send({"addr":66,"content":"ABC"})
    self.send_struct = {"addr":66,"content":"ABC"}
    """
    try:
        if not isinstance(info, dict):
            return "Error: info must be a dictionary"
        
        if "addr" not in info or "content" not in info:
            return "Error: info must contain 'addr' and 'content' keys"
        
        self.send_struct = info
        
    except Exception as e:
        return f"Error: {str(e)}"
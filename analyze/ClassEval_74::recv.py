class Server: 
    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

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
    
    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return "info structure is not correct"
        self.send_struct = {"addr": info["addr"], "content": info["content"]}
    
    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False
    
    def recv(self, info):
        """
        接收包含地址和内容的信息。如果地址在白名单上，则接收内容；否则，不接收
        :param info: dict，包含地址和内容的信息字典
        :return: 如果成功接收，返回信息的内容；否则，返回 False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return False
        if info["addr"] in self.white_list:
            self.receive_struct = {"addr": info["addr"], "content": info["content"]}
            return info["content"]
        return False
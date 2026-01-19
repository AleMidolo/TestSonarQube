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
    if type == 'send':
        return self.send_struct
    elif type == 'receive':
        return self.receive_struct
    else:
        return False
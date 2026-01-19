def show(self, type):
    """
    Devuelve la estructura del tipo especificado
    :param type: cadena, el tipo de estructura que se debe devolver, que puede ser 'send' o 'receive'
    :return: si type es igual a 'send' o 'receive', devuelve la estructura correspondiente; de lo contrario, devuelve False
    >>> server.recv({"addr":88,"content":"abc"})
    >>> server.send({"addr":66,"content":"ABC"})
    >>> server.show("send")
    {"addr":66,"content":"ABC"}
    """
    if type == 'send':
        return self.send_structure
    elif type == 'receive':
        return self.receive_structure
    else:
        return False
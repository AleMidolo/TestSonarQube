def show(self, type):
    """
        Restituisce la struttura del tipo specificato
        :param type: stringa, il tipo di struttura da restituire, che può essere 'send' o 'receive'
        :return: se type è uguale a 'send' o 'receive', restituisce la struttura corrispondente; altrimenti, restituisce False
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
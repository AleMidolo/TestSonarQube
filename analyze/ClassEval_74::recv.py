def recv(self, info):
    """
        Recibir información que contiene dirección y contenido. Si la dirección está en la lista blanca, recibir el contenido; de lo contrario, no recibirlo.
        :param info: dict, diccionario de información que contiene dirección y contenido
        :return: si se recibió con éxito, devolver el contenido de la información; de lo contrario, devolver False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return False
    if info['addr'] in self.white_list:
        self.receive_struct = {'addr': info['addr'], 'content': info['content']}
        return info['content']
    return False
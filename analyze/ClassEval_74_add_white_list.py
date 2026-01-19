def add_white_list(self, addr):
    """
        Agrega una dirección a la lista blanca y no hace nada si ya existe
        :param addr: int, dirección a ser agregada
        :return: nueva lista blanca, devuelve False si la dirección ya existe
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
    if addr in self.white_list:
        return False
    else:
        self.white_list.append(addr)
        return self.white_list
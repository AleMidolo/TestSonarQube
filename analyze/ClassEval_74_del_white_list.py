def del_white_list(self, addr):
    """
    Eliminar una dirección de la lista blanca y no hacer nada si no existe
    :param addr: int, dirección a eliminar
    :return: nueva lista blanca, devuelve False si la dirección no existe
    >>> server = Server()
    >>> server.add_white_list(88)
    >>> server.del_white_list(88)
    []
    """
    if addr in self.white_list:
        self.white_list.remove(addr)
        return self.white_list
    else:
        return False
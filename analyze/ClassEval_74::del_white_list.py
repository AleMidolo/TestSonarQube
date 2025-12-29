def del_white_list(self, addr):
    """
    Rimuovi un indirizzo dalla whitelist e non fare nulla se non esiste
    :param addr: int, indirizzo da eliminare
    :return: nuova whitelist, restituisce False se l'indirizzo non esiste
    >>> server = Server()
    >>> server.add_white_list(88)
    >>> server.del_white_list(88)
    []
    """
    if addr not in self.white_list:
        return False
    else:
        self.white_list.remove(addr)
        return self.white_list
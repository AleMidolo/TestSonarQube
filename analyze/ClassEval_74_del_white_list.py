def del_white_list(self, addr):
    """
    Rimuovi un indirizzo dalla whitelist e non fare nulla se non esiste
    :param addr: int, indirizzo da eliminare
    :return: nuova whitelist, restituisce False se l'indirizzo non esiste
    >>> server.add_white_list(88)
    >>> server.del_white_list(88)
    []
    """
    if not hasattr(self, 'white_list'):
        self.white_list = []
    
    if addr in self.white_list:
        self.white_list.remove(addr)
        return self.white_list
    else:
        return False
def add_white_list(self, addr):
    """
    Aggiungi un indirizzo alla whitelist e non fare nulla se esiste già
    :param addr: int, indirizzo da aggiungere
    :return: nuova whitelist, restituisce False se l'indirizzo esiste già
    >>> server = Server()
    >>> server.add_white_list(88)
    [88]
    """
    if not hasattr(self, 'white_list'):
        self.white_list = []
    
    if addr in self.white_list:
        return False
    
    self.white_list.append(addr)
    return self.white_list
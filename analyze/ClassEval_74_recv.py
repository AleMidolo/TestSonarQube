def recv(self, info):
    """
    Ricevi informazioni contenenti indirizzo e contenuto. Se l'indirizzo è nella whitelist, ricevi il contenuto; altrimenti, non riceverlo.
    :param info: dict, dizionario delle informazioni contenente indirizzo e contenuto
    :return: se ricevuto con successo, restituisci il contenuto delle informazioni; altrimenti, restituisci False
    >>> server.recv({"addr":88,"content":"abc"})
    abc
    """
    if hasattr(self, 'whitelist') and info.get('addr') in self.whitelist:
        return info.get('content')
    return False
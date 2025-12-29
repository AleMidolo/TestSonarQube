def recv(self, info):
    """
        Ricevi informazioni contenenti indirizzo e contenuto. Se l'indirizzo è nella whitelist, ricevi il contenuto; altrimenti, non riceverlo.
        :param info: dict, dizionario delle informazioni contenente indirizzo e contenuto
        :return: se ricevuto con successo, restituisci il contenuto delle informazioni; altrimenti, restituisci False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return False
    if info['addr'] in self.white_list:
        self.receive_struct = {'addr': info['addr'], 'content': info['content']}
        return info['content']
    return False
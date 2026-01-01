def send(self, info):
    """
        Invia informazioni contenenti indirizzo e contenuto
        :param info: dict, dizionario delle informazioni contenente indirizzo e contenuto
        :return: se inviato con successo, non restituisce nulla; altrimenti, restituisce una stringa che indica un messaggio di errore
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
    if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
        return 'Invalid input'
    self.send_struct = {'addr': info['addr'], 'content': info['content']}
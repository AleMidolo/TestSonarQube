def send(self, info):
    """
    Invia informazioni contenenti indirizzo e contenuto
    :param info: dict, dizionario delle informazioni contenente indirizzo e contenuto
    :return: se inviato con successo, non restituisce nulla; altrimenti, restituisce una stringa che indica un messaggio di errore
    >>> server.send({"addr":66,"content":"ABC"})
    self.send_struct = {"addr":66,"content":"ABC"}
    """
    try:
        if not isinstance(info, dict):
            return "Errore: info deve essere un dizionario"
        
        if "addr" not in info:
            return "Errore: indirizzo mancante"
        
        if "content" not in info:
            return "Errore: contenuto mancante"
        
        self.send_struct = info
        
    except Exception as e:
        return f"Errore durante l'invio: {str(e)}"
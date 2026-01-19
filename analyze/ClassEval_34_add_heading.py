def add_heading(self, heading, level=1):
    """
    Aggiunge un'intestazione al documento Word.
    :param heading: str, il testo dell'intestazione.
    :param level: int, opzionale, il livello dell'intestazione (1, 2, 3, ecc.; predefinito è 1).
    :return: bool, True se l'intestazione è stata aggiunta con successo, False altrimenti.
    """
    try:
        if not isinstance(heading, str):
            return False
        
        if not isinstance(level, int) or level < 1:
            return False
        
        # Assuming this is a method of a class that has a document object (e.g., python-docx)
        # self.document should be a Document instance from python-docx
        self.document.add_heading(heading, level=level)
        return True
    except Exception:
        return False
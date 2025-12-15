def add_heading(self, heading, level=1):
    """
    Aggiunge un'intestazione al documento Word.
    :param heading: str, il testo dell'intestazione.
    :param level: int, opzionale, il livello dell'intestazione (1, 2, 3, ecc.; predefinito è 1).
    :return: bool, True se l'intestazione è stata aggiunta con successo, False altrimenti.
    """
    
    try:
        doc = Document(self.file_path)
        doc.add_heading(heading, level=level)
        doc.save(self.file_path)
        return True
    except:
        return False
def read_json(self, file_path):
    """
        Leggi un file JSON e restituisci i dati.
        :param file_path: str, il percorso del file JSON.
        :return: dict, i dati dal file JSON se letti con successo, oppure restituisce -1 se si verifica un errore durante il processo di lettura.
                    restituisce 0 se il file non esiste.
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return -1
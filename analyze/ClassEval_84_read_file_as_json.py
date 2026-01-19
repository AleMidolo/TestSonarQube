def read_file_as_json(self):
    """
        Leggi il file self.file_path in formato json.
        Se il contenuto del file non rispetta il formato json, il codice solleverà un errore.
        :return data: dict se il file è memorizzato in formato json, o str/int/float.. a seconda del contenuto del file altrimenti.
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file_as_json()
        {'name': 'test', 'age': 12}
        >>> type(textFileProcessor.read_file_as_json())
        <class 'dict'>
        """
    with open(self.file_path, 'r') as file:
        return json.load(file)
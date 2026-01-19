def read_file(self):
    """
        Leggi e restituisci il contenuto del file self.file_path.
        :return: lo stesso valore restituito dal metodo read()
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{
    "name": "test",
    "age": 12
}'
        """
    with open(self.file_path, 'r') as file:
        return file.read()
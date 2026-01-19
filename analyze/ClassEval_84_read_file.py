def read_file(self):
    """
    Leggi e restituisci il contenuto del file self.file_path.
    :return: lo stesso valore restituito dal metodo read()
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    """
    with open(self.file_path, 'r') as file:
        return file.read()
def read_file(self):
    """
        Lee y devuelve el contenido del archivo self.file_path.
        :return: el mismo retorno que el método read()
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{
    "name": "test",
    "age": 12
}'
        """
    with open(self.file_path, 'r') as file:
        return file.read()
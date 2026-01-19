def read_file(self):
    """
    Read the return the content of self.file_path file.
    :return: the same return as the read() method
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    """
    with open(self.file_path, 'r') as file:
        return file.read()
def write_file(self, content):
    """
    Write content into the self.file_path file, and overwrite if the file has already existed.
    :param content: any content
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.write_file('Hello world!')
    >>> textFileProcessor.read_file()
    'Hello world!'
    """
    with open(self.file_path, 'w') as file:
        file.write(content)
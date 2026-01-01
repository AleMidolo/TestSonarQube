def write_file(self, content):
    """
        Scrive il contenuto nel file self.file_path, sovrascrivendo se il file esiste già.
        :param content: qualsiasi contenuto
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """
    with open(self.file_path, 'w') as file:
        file.write(content)
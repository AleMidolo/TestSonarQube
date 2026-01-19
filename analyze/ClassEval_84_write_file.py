def write_file(self, content):
    """
        Write the content to the self.file_path file, overwriting if the file already exists.
        :param content: any content
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """
    with open(self.file_path, 'w') as file:
        file.write(content)
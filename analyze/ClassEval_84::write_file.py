def write_file(self, content):
    """
        将内容写入 self.file_path 文件，如果文件已存在则覆盖。
        :param content: 任何内容
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """
    with open(self.file_path, 'w') as file:
        file.write(str(content))
def read_file(self):
    """
        读取并返回 self.file_path 文件的内容。
        :return: 与 read() 方法相同的返回值
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{
    "name": "test",
    "age": 12
}'
        """
    with open(self.file_path, 'r') as file:
        content = file.read()
    return content
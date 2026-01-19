def process_file(self):
    """
        读取 self.file_path 文件，并从内容字符串中过滤掉非字母字符。
        将处理后的数据覆盖写入同一个 self.file_path 文件。
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{
    "name": "test",
    "age": 12
}'
        >>> textFileProcessor.process_file()
        'nametestage'
        """
    content = self.read_file()
    filtered_content = ''.join(filter(str.isalpha, content))
    self.write_file(filtered_content)
    return filtered_content
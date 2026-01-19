def read_file_as_json(self):
    """
        以 json 格式读取 self.file_path 文件。
        如果文件内容不符合 json 格式，代码将引发错误。
        :return data: 如果文件以 json 格式存储，则返回 dict，否则根据文件内容返回 str/int/float 等。
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file_as_json()
        {'name': 'test', 'age': 12}
        >>> type(textFileProcessor.read_file_as_json())
        <class 'dict'>
        """
    with open(self.file_path, 'r') as file:
        return json.load(file)
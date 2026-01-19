def process_file(self):
    """
    读取 self.file_path 文件，并从内容字符串中过滤掉非字母字符。
    将处理后的数据覆盖写入同一个 self.file_path 文件。
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    >>> textFileProcessor.process_file()
    'nametestage'
    """
    # 读取文件内容
    with open(self.file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 过滤掉非字母字符
    processed_content = ''.join(char for char in content if char.isalpha())
    
    # 将处理后的数据覆盖写入同一个文件
    with open(self.file_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    return processed_content
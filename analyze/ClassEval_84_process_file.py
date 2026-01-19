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
    # Read the file content
    with open(self.file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Filter out non-alphabetic characters
    processed_content = ''.join(char for char in content if char.isalpha())
    
    # Write the processed content back to the same file
    with open(self.file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)
    
    return processed_content
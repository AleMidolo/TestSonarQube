def process_file(self):
    """
    Read the self.file_path file and filter out non-alphabetic characters from the content string.
    Overwrite the after-processed data into the same self.file_path file.
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    >>> textFileProcessor.process_file()
    'nametestage'
    """
    with open(self.file_path, 'r') as file:
        content = file.read()
    
    filtered_content = ''.join(char for char in content if char.isalpha())
    
    with open(self.file_path, 'w') as file:
        file.write(filtered_content)
    
    return filtered_content
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
    # Read the file content
    with open(self.file_path, 'r') as file:
        content = file.read()
    
    # Filter out non-alphabetic characters
    processed_content = ''.join(char for char in content if char.isalpha())
    
    # Overwrite the file with processed content
    with open(self.file_path, 'w') as file:
        file.write(processed_content)
    
    return processed_content
def process_file(self):
    """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
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
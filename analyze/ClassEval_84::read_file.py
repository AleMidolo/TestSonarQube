def read_file(self):
        """
        self.file_path फ़ाइल की सामग्री पढ़ें और लौटाएं।
        :return: read() विधि के समान लौटाएं
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{\n    "name": "test",\n    "age": 12\n}'
        """
        with open(self.file_path, 'r') as file:
            return file.read()
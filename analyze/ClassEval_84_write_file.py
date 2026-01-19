def write_file(self, content):
    """
        सामग्री को self.file_path फ़ाइल में लिखें, और यदि फ़ाइल पहले से मौजूद है तो उसे ओवरराइट करें।
        :param content: कोई भी सामग्री
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """
    with open(self.file_path, 'w') as file:
        file.write(str(content))
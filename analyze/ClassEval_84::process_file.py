def process_file(self):
    """
    self.file_path फ़ाइल को पढ़ें और सामग्री स्ट्रिंग से गैर-अक्षर वर्णों को फ़िल्टर करें।
    प्रोसेस किए गए डेटा को उसी self.file_path फ़ाइल में ओवरराइट करें।
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
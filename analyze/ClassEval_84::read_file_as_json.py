def read_file_as_json(self):
        """
        self.file_path फ़ाइल को json प्रारूप के रूप में पढ़ें।
        यदि फ़ाइल की सामग्री json प्रारूप का पालन नहीं करती है, तो कोड त्रुटि उत्पन्न करेगा।
        :return data: यदि फ़ाइल json प्रारूप में संग्रहीत है तो dict, अन्यथा फ़ाइल की सामग्री के अनुसार str/int/float..
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file_as_json()
        {'name': 'test', 'age': 12}
        >>> type(textFileProcessor.read_file_as_json())
        <class 'dict'>
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)
def process_file(self):
    """
        Lee el archivo self.file_path y filtra los caracteres no alfabéticos de la cadena de contenido.
        Sobrescribe los datos procesados en el mismo archivo self.file_path.
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
    filtered_content = re.sub('[^a-zA-Z]', '', content)
    self.write_file(filtered_content)
    return filtered_content
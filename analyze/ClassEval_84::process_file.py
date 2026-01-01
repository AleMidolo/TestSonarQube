def process_file(self):
    """
    Leggi il file self.file_path e filtra i caratteri non alfabetici dalla stringa di contenuto.
    Sovrascrivi i dati dopo l'elaborazione nello stesso file self.file_path.
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
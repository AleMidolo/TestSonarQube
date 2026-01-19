def process_file(self):
    """
    Leggi il file self.file_path e filtra i caratteri non alfabetici dalla stringa di contenuto.
    Sovrascrivi i dati dopo l'elaborazione nello stesso file self.file_path.
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    >>> textFileProcessor.process_file()
    'nametestage'
    """
    # Leggi il contenuto del file
    with open(self.file_path, 'r') as file:
        content = file.read()
    
    # Filtra solo i caratteri alfabetici
    filtered_content = ''.join(char for char in content if char.isalpha())
    
    # Sovrascrivi il file con il contenuto filtrato
    with open(self.file_path, 'w') as file:
        file.write(filtered_content)
    
    return filtered_content
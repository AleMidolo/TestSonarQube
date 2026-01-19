def process_file(self):
    """
    Lee el archivo self.file_path y filtra los caracteres no alfabéticos de la cadena de contenido.
    Sobrescribe los datos procesados en el mismo archivo self.file_path.
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file()
    '{\n    "name": "test",\n    "age": 12\n}'
    >>> textFileProcessor.process_file()
    'nametestage'
    """
    # Leer el contenido del archivo
    with open(self.file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Filtrar solo caracteres alfabéticos
    processed_content = ''.join(char for char in content if char.isalpha())
    
    # Sobrescribir el archivo con el contenido procesado
    with open(self.file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)
    
    return processed_content
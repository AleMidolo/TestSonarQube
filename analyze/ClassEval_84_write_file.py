def write_file(self, content):
    """
        Escribe contenido en el archivo self.file_path, y sobrescribe si el archivo ya existía.
        :param content: cualquier contenido
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('¡Hola mundo!')
        >>> textFileProcessor.read_file()
        '¡Hola mundo!'
        """
    with open(self.file_path, 'w') as file:
        file.write(content)
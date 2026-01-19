def read_file_as_json(self):
    """
    Lee el archivo self.file_path en formato json.
    Si el contenido del archivo no cumple con el formato json, el código generará un error.
    :return data: dict si el archivo está almacenado en formato json, o str/int/float.. según el contenido del archivo en caso contrario.
    >>> textFileProcessor = TextFileProcessor('test.json')
    >>> textFileProcessor.read_file_as_json()
    {'name': 'test', 'age': 12}
    >>> type(textFileProcessor.read_file_as_json())
    <class 'dict'>
    """
    with open(self.file_path, 'r') as file:
        return json.load(file)
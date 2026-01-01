def read_json(self, file_path):
    """
        Lee un archivo JSON y devuelve los datos.
        :param file_path: str, la ruta del archivo JSON.
        :return: dict, los datos del archivo JSON si se leen correctamente, o devuelve -1 si ocurre un error durante el proceso de lectura.
                    devuelve 0 si el archivo no existe.
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return -1
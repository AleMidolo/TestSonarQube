def write_json(self, data, file_path):
    """
    Escribe datos en un archivo JSON y los guarda en la ruta dada.

    :param data: dict, los datos que se escribirán en el archivo JSON.
    :param file_path: str, la ruta del archivo JSON.
    :return: 1 si el proceso de escritura es exitoso, o -1 si ocurre un error durante el proceso de escritura.
    >>> json.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
    1
    >>> json.read_json('test.json')
    {'key1': 'value1', 'key2': 'value2'}
    """
    import json
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return 1
    except Exception:
        return -1
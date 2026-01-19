def insert(self, data):
    """
        Genera una declaración SQL INSERT basada en los datos proporcionados.
        :param data: dict. Los datos a insertar, en forma de diccionario donde las claves son nombres de campos y los valores son valores de campos.
        :return: str. La declaración SQL generada.
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """
    columns = ', '.join(data.keys())
    values = ', '.join((f"'{value}'" for value in data.values()))
    return f'INSERT INTO {self.table_name} ({columns}) VALUES ({values});'
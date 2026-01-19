def insert(self, data):
    """
    Genera una declaración SQL INSERT basada en los datos proporcionados.
    :param data: dict. Los datos a insertar, en forma de diccionario donde las claves son nombres de campos y los valores son valores de campos.
    :return: str. La declaración SQL generada.
    >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
    "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
    """
    if not data:
        return ""
    
    # Obtener las columnas y valores
    columns = ', '.join(data.keys())
    
    # Formatear los valores: agregar comillas simples a strings
    values = []
    for value in data.values():
        if isinstance(value, str):
            # Escapar comillas simples en el valor
            escaped_value = value.replace("'", "''")
            values.append(f"'{escaped_value}'")
        elif value is None:
            values.append('NULL')
        elif isinstance(value, bool):
            values.append('TRUE' if value else 'FALSE')
        else:
            values.append(str(value))
    
    values_str = ', '.join(values)
    
    # Asumir que self.table_name contiene el nombre de la tabla
    table_name = getattr(self, 'table_name', 'table1')
    
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});"
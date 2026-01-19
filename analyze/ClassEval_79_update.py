def update(self, data, condition):
    """
        Genera una declaración SQL UPDATE basada en los datos y la condición dados.
        :param data: dict. Los datos a ser actualizados, en forma de diccionario donde las claves son nombres de campos y los valores son nuevos valores de campo.
        :param condition: str. La expresión de condición para la actualización.
        :return: str. La declaración SQL generada.
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
    sql = f'UPDATE {self.table_name} SET {set_clause} WHERE {condition}'
    return sql + ';'
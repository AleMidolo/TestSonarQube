def update(self, data, condition):
    """
    Genera una declaración SQL UPDATE basada en los datos y la condición dados.
    :param data: dict. Los datos a ser actualizados, en forma de diccionario donde las claves son nombres de campos y los valores son nuevos valores de campo.
    :param condition: str. La expresión de condición para la actualización.
    :return: str. La declaración SQL generada.
    >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
    "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
    """
    set_clauses = []
    for field, value in data.items():
        if isinstance(value, str):
            set_clauses.append(f"{field} = '{value}'")
        else:
            set_clauses.append(f"{field} = {value}")
    
    set_statement = ", ".join(set_clauses)
    sql_statement = f"UPDATE {self.table} SET {set_statement} WHERE {condition};"
    
    return sql_statement
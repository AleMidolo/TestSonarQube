def delete(self, condition):
    """
    Genera una declaración SQL DELETE basada en la condición dada.
    :param condition: str. La expresión de condición para la eliminación.
    :return: str. La declaración SQL generada.
    >>> sql.delete("field1 = value1")
    'DELETE FROM table1 WHERE field1 = value1;'
    """
    return f"DELETE FROM {self.table_name} WHERE {condition};"
def delete(self, condition):
    """
        Genera un'istruzione SQL DELETE basata sulla condizione fornita.
        :param condition: str. L'espressione di condizione per la cancellazione.
        :return: str. L'istruzione SQL generata.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """
    sql = f'DELETE FROM {self.table_name} WHERE {condition}'
    return sql + ';'
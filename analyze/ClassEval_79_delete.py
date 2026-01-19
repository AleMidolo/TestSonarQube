def delete(self, condition):
    """
    Generates a DELETE SQL statement based on the given condition.
    :param condition: str. The condition expression for the delete.
    :return: str. The generated SQL statement.
    >>> sql.delete("field1 = value1")
    'DELETE FROM table1 WHERE field1 = value1;'
    """
    return f"DELETE FROM {self.table} WHERE {condition};"
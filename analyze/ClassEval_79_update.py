def update(self, data, condition):
    """
    Generates an UPDATE SQL statement based on the given data and condition.
    :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
    :param condition: str. The condition expression for the update.
    :return: str. The generated SQL statement.
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
def delete(self, condition):
    """
    根据给定的条件生成一个 DELETE SQL 语句。
    :param condition: str. 删除的条件表达式。
    :return: str. 生成的 SQL 语句。
    >>> sql.delete("field1 = value1")
    'DELETE FROM table1 WHERE field1 = value1;'
    """
    return f"DELETE FROM {self.table_name} WHERE {condition};"
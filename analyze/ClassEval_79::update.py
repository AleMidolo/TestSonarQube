def update(self, data, condition):
    """
        根据给定的数据和条件生成一个 UPDATE SQL 语句。
        :param data: dict. 要更新的数据，以字典形式表示，其中键是字段名，值是新的字段值。
        :param condition: str. 更新的条件表达式。
        :return: str. 生成的 SQL 语句。
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
    sql = f'UPDATE {self.table_name} SET {set_clause} WHERE {condition}'
    return sql + ';'
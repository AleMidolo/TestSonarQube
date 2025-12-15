class SQLQueryBuilder: 

    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
    
        if columns != '*':
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += " WHERE " + \
                    ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
    
    @staticmethod
    def insert(table, data):
        """
            Generate the INSERT SQL statement from the given parameters.
            :param table: str, the table to be inserted in database.
            :param data: dict, the key and value in SQL insert statement
            :return query: str, the SQL insert statement.
            >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
            "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
            """
    
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        return f"INSERT INTO {table} ({keys}) VALUES ({values})"
    
    @staticmethod
    def update(table, data, where=None):
        """
            Generate the UPDATE SQL statement from the given parameters.
            :param table: str, the table that will be excuted with UPDATE operation in database
            :param data: dict, the key and value in SQL update statement
            :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
            >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
            "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
            """
    
        update_str = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {update_str}"
        if where:
            query += " WHERE " + \
                    ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
    
    @staticmethod
    def delete(table, where=None):
        """
        Genera l'istruzione SQL DELETE dai parametri forniti.
        :param table: str, la tabella che verrà eseguita con l'operazione DELETE nel database
        :param where: dict, {key1: value1, key2: value2 ...}. La condizione della query.
        :return query: str, l'istruzione SQL delete.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        query = f"DELETE FROM {table}"
        if where:
            query += " WHERE " + \
                    ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
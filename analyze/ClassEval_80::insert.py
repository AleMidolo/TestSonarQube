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
    def delete(table, where=None):
        """
            Generate the DELETE SQL statement from the given parameters.
            :param table: str, the table that will be excuted with DELETE operation in database
            :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
            :return query: str, the SQL delete statement.
            >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
            "DELETE FROM table1 WHERE name='Test' AND age='14'"
            """
    
        query = f"DELETE FROM {table}"
        if where:
            query += " WHERE " + \
                    ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
    
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
    def insert(table, data):
        """
        Genera l'istruzione SQL INSERT dai parametri forniti.
        :param table: str, la tabella in cui inserire nel database.
        :param data: dict, la chiave e il valore nell'istruzione SQL di inserimento
        :return query: str, l'istruzione SQL di inserimento.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"
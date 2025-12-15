class SQLQueryBuilder: 

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
    def select(table, columns='*', where=None):
        """
        दिए गए पैरामीटर से SELECT SQL कथन उत्पन्न करें।
        :param table: str, डेटाबेस में क्वेरी तालिका।
        :param columns: str की सूची, ['col1', 'col2']।
        :param where: dict, {key1: value1, key2: value2 ...}. क्वेरी की शर्त।
        return query: str, SQL क्वेरी कथन।
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
        
        columns_str = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {columns_str} FROM {table}"
        if where:
            query += " WHERE " + \
                    ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
def search_database(self, table_name, name):
        """
        在数据库中搜索指定表中具有匹配名称的行。
        :param table_name: str，要搜索的表的名称。
        :param name: str，要搜索的名称。
        :return: list, 一个元组列表，表示具有匹配名称的行（如果有的话）；否则返回 None。
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        search_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(search_query, (name,))
        results = cursor.fetchall()
        
        conn.close()
        
        return results if results else None
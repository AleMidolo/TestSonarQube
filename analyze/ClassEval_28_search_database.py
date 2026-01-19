def search_database(self, table_name, name):
    """
    在数据库中搜索指定表中具有匹配名称的行。
    :param table_name: str，要搜索的表的名称。
    :param name: str，要搜索的名称。
    :return: list, 一个元组列表,表示具有匹配名称的行(如果有的话);否则返回 None。
    >>> db.search_database('user', 'John')
    [(1, 'John', 25)]
    """
    cursor = self.connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", (name,))
    result = cursor.fetchall()
    cursor.close()
    
    if result:
        return result
    else:
        return None
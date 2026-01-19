def search_database(self, table_name, name):
    """
    在数据库中搜索指定表中具有匹配名称的行。
    :param table_name: str，要搜索的表的名称。
    :param name: str，要搜索的名称。
    :return: list, 一个元组列表，表示具有匹配名称的行（如果有的话）；否则返回 None。
    >>> db.search_database('user', 'John')
    [(1, 'John', 25)]
    """
    cursor = self.connection.cursor()
    
    # 使用参数化查询防止SQL注入
    # 假设name字段是表中的第二列（常见的数据库设计）
    query = f"SELECT * FROM {table_name} WHERE name = ?"
    
    cursor.execute(query, (name,))
    results = cursor.fetchall()
    
    if results:
        return results
    else:
        return None
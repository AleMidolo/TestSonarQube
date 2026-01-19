def delete_from_database(self, table_name, name):
    """
    从数据库中指定的表中删除匹配名称的行。
    :param table_name: str，要从中删除行的表的名称。
    :param name: str，要匹配以进行删除的名称。
    >>> db.delete_from_database('user', 'John')
    """
    import sqlite3
    
    if not hasattr(self, 'connection') or self.connection is None:
        raise Exception("Database connection not established")
    
    cursor = self.connection.cursor()
    
    # 使用参数化查询防止SQL注入
    query = f"DELETE FROM {table_name} WHERE name = ?"
    cursor.execute(query, (name,))
    
    self.connection.commit()
    cursor.close()
def delete_from_database(self, table_name, name):
    """
        从数据库中指定的表中删除匹配名称的行。
        :param table_name: str，要从中删除行的表的名称。
        :param name: str，要匹配以进行删除的名称。
        >>> db.delete_from_database('user', 'John')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_info = cursor.fetchall()
    name_column = None
    for col_info in columns_info:
        if col_info[2].upper() == 'TEXT':
            name_column = col_info[1]
            break
    if name_column:
        delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(delete_query, (name,))
    elif len(columns_info) > 1:
        name_column = columns_info[1][1]
        delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()
def delete_from_database(self, table_name, name):
    """
        Elimina filas de la tabla especificada en la base de datos que coincidan con el nombre.
        :param table_name: str, el nombre de la tabla de la que eliminar filas.
        :param name: str, el nombre a coincidir para la eliminación.
        >>> db.delete_from_database('user', 'John')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_info = cursor.fetchall()
    text_column = None
    for col_info in columns_info:
        if col_info[2] == 'TEXT':
            text_column = col_info[1]
            break
    if text_column:
        delete_query = f'DELETE FROM {table_name} WHERE {text_column} = ?'
        cursor.execute(delete_query, (name,))
    else:
        select_query = f'SELECT * FROM {table_name}'
        cursor.execute(select_query)
        all_rows = cursor.fetchall()
        for row in all_rows:
            if name in row:
                pk_column = None
                for col_info in columns_info:
                    if col_info[5] == 1:
                        pk_column = col_info[1]
                        break
                if pk_column:
                    delete_query = f'DELETE FROM {table_name} WHERE {pk_column} = ?'
                    cursor.execute(delete_query, (row[0],))
    conn.commit()
    conn.close()
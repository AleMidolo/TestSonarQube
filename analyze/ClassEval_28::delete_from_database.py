def delete_from_database(self, table_name, name):
    """
        Elimina filas de la tabla especificada en la base de datos que coincidan con el nombre.
        :param table_name: str, el nombre de la tabla de la que eliminar filas.
        :param name: str, el nombre a coincidir para la eliminación.
        >>> db.delete_from_database('user', 'John')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    delete_query = f'DELETE FROM {table_name} WHERE name = ?'
    cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()
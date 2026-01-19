def delete_from_database(self, table_name, name):
    """
    Elimina filas de la tabla especificada en la base de datos que coincidan con el nombre.
    :param table_name: str, el nombre de la tabla de la que eliminar filas.
    :param name: str, el nombre a coincidir para la eliminación.
    >>> db.delete_from_database('user', 'John')
    """
    cursor = self.connection.cursor()
    query = f"DELETE FROM {table_name} WHERE name = ?"
    cursor.execute(query, (name,))
    self.connection.commit()
    cursor.close()
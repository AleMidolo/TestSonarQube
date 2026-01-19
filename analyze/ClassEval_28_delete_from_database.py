def delete_from_database(self, table_name, name):
    """
    Delete rows from the specified table in the database with a matching name.
    :param table_name: str, the name of the table to delete rows from.
    :param name: str, the name to match for deletion.
    >>> db.delete_from_database('user', 'John')
    """
    query = f"DELETE FROM {table_name} WHERE name = ?"
    self.cursor.execute(query, (name,))
    self.connection.commit()
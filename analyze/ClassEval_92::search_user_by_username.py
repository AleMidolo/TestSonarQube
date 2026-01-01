def search_user_by_username(self, username):
    """
        Busca usuarios en la tabla "users" por nombre de usuario.
        :param username: str, el nombre de usuario del usuario a buscar.
        :return: lista de tuplas, las filas de la tabla "users" que coinciden con los criterios de búsqueda.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT * FROM users WHERE username = ?\n        ', (username,))
    result = self.cursor.fetchone()
    return result
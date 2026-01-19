def delete_user_by_username(self, username):
    """
        Elimina un usuario de la tabla "users" por nombre de usuario.
        :param username: str, el nombre de usuario del usuario a eliminar.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """
    self.cursor.execute('\n                DELETE FROM users WHERE username = ?\n            ', (username,))
    self.connection.commit()
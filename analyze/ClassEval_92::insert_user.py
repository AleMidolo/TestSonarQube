def insert_user(self, username, password):
    """
        Inserta un nuevo usuario en la tabla "users".
        :param username: str, el nombre de usuario del usuario.
        :param password: str, la contraseña del usuario.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
    self.cursor.execute('\n                INSERT INTO users (username, password) VALUES (?, ?)\n            ', (username, password))
    self.connection.commit()
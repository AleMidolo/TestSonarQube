def validate_user_login(self, username, password):
    """
        Determina si el usuario puede iniciar sesión, es decir, si el usuario está en la base de datos y la contraseña es correcta
        :param username:str, el nombre de usuario del usuario a validar.
        :param password:str, la contraseña del usuario a validar.
        :return:bool, que representa si el usuario puede iniciar sesión correctamente
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.validate_user_login('user1', 'pass1')
        True
        """
    self.cursor.execute('\n                SELECT * FROM users WHERE username = ? AND password = ?\n            ', (username, password))
    user = self.cursor.fetchone()
    return user is not None
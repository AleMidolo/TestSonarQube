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
    user = self.search_user_by_username(username)
    if user is None:
        return False
    stored_password = user[2]
    return stored_password == password
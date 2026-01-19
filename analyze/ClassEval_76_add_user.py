def add_user(self, username):
    """
    Agrega un usuario al sistema de inicio de sesión si el usuario no está en self.users.
    Y el estado inicial es False.
    :param username: str, el nombre de usuario que se va a agregar.
    :return: bool, True si el usuario se agrega con éxito, False si el usuario ya existe.
    >>> signInSystem.add_user("mike")
    True
    >>> signInSystem.add_user("mike")
    False
    """
    if username in self.users:
        return False
    else:
        self.users[username] = False
        return True
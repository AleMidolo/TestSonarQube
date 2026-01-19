def sign_in(self, username):
    """
    Iniciar sesión de un usuario si el usuario está en self.users y cambiar el estado a True.
    :param username: str, el nombre de usuario que se va a iniciar sesión.
    :return: bool, True si el usuario ha iniciado sesión con éxito, False si el usuario no existe.
    >>> signInSystem.sign_in("mike")
    True
    >>> signInSystem.sign_in("mik")
    False
    """
    if username in self.users:
        self.users[username] = True
        return True
    return False
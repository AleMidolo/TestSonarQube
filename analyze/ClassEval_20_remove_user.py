def remove_user(self, username):
    """
    Eliminar un usuario del Chat.
    :param username: El nombre del usuario, str.
    :return: Si el usuario ya está en el Chat, devuelve True, de lo contrario, devuelve False.
    >>> chat = Chat()
    >>> chat.users = {'John': []}
    >>> chat.remove_user('John')
    True
    >>> chat.remove_user('John')
    False

    """
    if username in self.users:
        del self.users[username]
        return True
    return False
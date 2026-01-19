def add_user(self, username):
    """
    Agrega un nuevo usuario al Chat.
    :param username: El nombre del usuario, str.
    :return: Si el usuario ya está en el Chat, devuelve False, de lo contrario, devuelve True.
    >>> chat = Chat()
    >>> chat.add_user('John')
    True
    self.users = {'John': []}
    >>> chat.add_user('John')
    False

    """
    if username in self.users:
        return False
    else:
        self.users[username] = []
        return True
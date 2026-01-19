def get_messages(self, username):
    """
    Obtiene todos los mensajes de un usuario del Chat.
    :param username: El nombre del usuario, str.
    :return: Una lista de mensajes, cada mensaje es un diccionario con las claves 'sender', 'receiver', 'message', 'timestamp'.
    >>> chat = Chat()
    >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
    >>> chat.get_messages('John')
    [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
    >>> chat.get_messages('Mary')
    []

    """
    if username in self.users:
        return self.users[username]
    else:
        return []
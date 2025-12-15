def add_user(self, username):
    """
    Aggiungi un nuovo utente alla Chat.
    :param username: Il nome dell'utente, str.
    :return: Se l'utente è già nella Chat, restituisce False, altrimenti restituisce True.
    >>> chat = Chat()
    >>> chat.add_user('John')
    True
    >>> chat.users
    {'John': []}
    >>> chat.add_user('John')
    False

    """
    
    if username in self.users:
        return False
    else:
        self.users[username] = []
        return True
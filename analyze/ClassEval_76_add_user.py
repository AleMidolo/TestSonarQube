def add_user(self, username):
    """
    Aggiungi un utente al sistema di accesso se l'utente non è già presente in self.users.
    E lo stato iniziale è False.
    :param username: str, il nome utente da aggiungere.
    :return: bool, True se l'utente è stato aggiunto con successo, False se l'utente esiste già.
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
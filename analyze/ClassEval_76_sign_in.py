def sign_in(self, username):
    """
    Accedi a un utente se l'utente è presente in self.users e cambia lo stato a True.
    :param username: str, il nome utente da accedere.
    :return: bool, True se l'utente è stato autenticato con successo, False se l'utente non esiste.
    >>> signInSystem.sign_in("mike")
    True
    >>> signInSystem.sign_in("mik")
    False
    """
    if username in self.users:
        self.users[username] = True
        return True
    return False
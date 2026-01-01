def check_sign_in(self, username):
    """
        Controlla se un utente è connesso.
        :param username: str, il nome utente da controllare.
        :return: bool, True se l'utente è connesso, False se l'utente non esiste o non è connesso.
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """
    if username not in self.users or not self.users[username]:
        return False
    return True
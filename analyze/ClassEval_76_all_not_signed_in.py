def all_not_signed_in(self):
    """
    Ottieni un elenco di nomi utente che non sono connessi.
    :return: list[str], un elenco di nomi utente che non sono connessi.
    >>> signInSystem = SignInSystem()
    >>> signInSystem.add_user("a")
    True
    >>> signInSystem.add_user("b")
    True
    >>> signInSystem.all_not_signed_in()
    ['a', 'b']
    """
    return [username for username, signed_in in self.users.items() if not signed_in]
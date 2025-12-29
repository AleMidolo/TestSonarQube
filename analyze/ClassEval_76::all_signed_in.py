def all_signed_in(self):
    """
        Controlla se tutti gli utenti sono connessi.
        :return: bool, True se tutti gli utenti sono connessi, False altrimenti.
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """
    if not self.users:
        return True
    return all(self.users.values())
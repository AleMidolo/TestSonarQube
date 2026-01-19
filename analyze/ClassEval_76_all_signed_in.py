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
    if not hasattr(self, 'users') or len(self.users) == 0:
        return True
    
    if not hasattr(self, 'signed_in_users'):
        return False
    
    return len(self.signed_in_users) == len(self.users)
def all_signed_in(self):
    """
    Verifica si todos los usuarios han iniciado sesión.
    :return: bool, True si todos los usuarios han iniciado sesión, False en caso contrario.
    >>> signInSystem.add_user("jack")
    True
    >>> signInSystem.sign_in("jack")
    >>> signInSystem.all_signed_in()
    True
    """
    if not hasattr(self, 'users') or not self.users:
        return True
    
    if not hasattr(self, 'signed_in_users'):
        return False
    
    return len(self.signed_in_users) == len(self.users)
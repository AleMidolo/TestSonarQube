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
    return all((signed_in for signed_in in self.users.values()))
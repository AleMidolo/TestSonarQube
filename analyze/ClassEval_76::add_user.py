class SignInSystem: 
    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}

    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        >>> signInSystem.sign_in("mike")
        True
        >>> signInSystem.sign_in("mik")
        False
        """
        if username not in self.users:
            return False
        else:
            self.users[username] = True
            return True
    
    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """
        if username not in self.users:
            return False
        else:
            return self.users[username]
    
    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """
        return all(self.users.values())
    
    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """
        return [username for username, signed_in in self.users.items() if not signed_in]
    
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
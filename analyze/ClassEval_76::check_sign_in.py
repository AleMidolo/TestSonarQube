class SignInSystem: 
    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
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
        if all(self.users.values()):
            return True
        else:
            return False
    
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
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users
    
    def check_sign_in(self, username):
        """
        जांचें कि क्या एक उपयोगकर्ता साइन इन है।
        :param username: str, जांचने के लिए उपयोगकर्ता नाम।
        :return: bool, True यदि उपयोगकर्ता साइन इन है, False यदि उपयोगकर्ता मौजूद नहीं है या साइन इन नहीं है।
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
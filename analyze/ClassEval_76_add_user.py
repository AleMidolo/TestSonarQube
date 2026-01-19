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
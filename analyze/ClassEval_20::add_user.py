def add_user(self, username):
    """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        >>> chat.users = {'John': []}
        >>> chat.add_user('John')
        False
        """
    if username in self.users:
        return False
    self.users[username] = []
    return True
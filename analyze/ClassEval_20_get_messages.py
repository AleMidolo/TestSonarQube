def get_messages(self, username):
    """
    Get all the messages of a user from the Chat.
    :param username: The user's name, str.
    :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
    >>> chat = Chat()
    >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
    >>> chat.get_messages('John')
    [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
    >>> chat.get_messages('Mary')
    []

    """
    return self.users.get(username, [])
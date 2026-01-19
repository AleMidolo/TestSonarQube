def add_user(self, username):
    """
    向聊天中添加新用户。
    :param username: 用户的名称，str。
    :return: 如果用户已经在聊天中，则返回 False，否则返回 True。
    >>> chat = Chat()
    >>> chat.add_user('John')
    True
    self.users = {'John': []}
    >>> chat.add_user('John')
    False

    """
    if username in self.users:
        return False
    else:
        self.users[username] = []
        return True
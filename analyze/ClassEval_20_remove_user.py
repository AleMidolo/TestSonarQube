def remove_user(self, username):
    """
    从聊天中移除用户。
    :param username: 用户的名称，字符串。
    :return: 如果用户已经在聊天中，返回 True；否则，返回 False。
    >>> chat = Chat()
    >>> chat.users = {'John': []}
    >>> chat.remove_user('John')
    True
    >>> chat.remove_user('John')
    False

    """
    if username in self.users:
        del self.users[username]
        return True
    else:
        return False
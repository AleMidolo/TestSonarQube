def add_user(self, username):
    """
    如果用户不在 self.users 中，则将用户添加到登录系统。
    初始状态为 False。
    :param username: str，要添加的用户名。
    :return: bool，如果用户成功添加则返回 True，如果用户已存在则返回 False。
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